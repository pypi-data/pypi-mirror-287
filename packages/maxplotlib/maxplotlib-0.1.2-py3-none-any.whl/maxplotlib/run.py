import base64
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mlx.core as mx
import mlx.nn as nn
from mlx_lm import load, generate
from mlx_lm.tokenizer_utils import TokenizerWrapper
from mlx_lm.utils import apply_repetition_penalty
import numpy as np
from PIL import Image
import time
from typing import Any, Callable, Dict, Generator, List, Optional, Tuple, Union

model, tokenizer = load("mlx-community/Meta-Llama-3.1-8B-Instruct-4bit")

# llama 3.1 info from meta prompt guide
# https://llama.meta.com/docs/model-cards-and-prompt-formats/llama3_1

prompt_template = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Cutting Knowledge Date: December 2023
Today Date: 23 Jul 2024

You are a helpful assistant<|eot_id|>
<|start_header_id|>user<|end_header_id|>

{user_message}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""

brainstorm_matplotlib_template = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Cutting Knowledge Date: December 2023
Today Date: 23 Jul 2024

You turn a user request into as many incredible ideas for matplotlib visualizations as possible.
Your ideas are fully self-contained and geared towards being implemented directly using matplotlib and numpy.
You always respond with {num_ideas} ideas like this:
IDEAS:
* idea 1 * first idea
...
* idea {num_ideas} * last idea
You are a helpful assistant<|eot_id|><|start_header_id|>user<|end_header_id|>

{user_message}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""

ipython_start_tag = "<|python_tag|>"
ipython_end_tag = "<|eom_id|>"
matplotlib_numpy_prompt_template = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython

Cutting Knowledge Date: December 2023
Today Date: 23 Jul 2024

# Tool Instructions
- You always start with
<|python_tag|>import matplotlib.pyplot as plt
import numpy as np
- The only non-standard Python libraries that are allowed are matplotlib and numpy
- All figures need to have titles, and each subplot needs a title & axis labels

You are a helpful assistant<|eot_id|>
<|start_header_id|>user<|end_header_id|>

{user_message}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""

# mlx batch generation code from MLX Para-LLM (Will Brown)
# https://github.com/willccbb/mlx_parallm/tree/main

class BatchedKVCache:

    def __init__(self, head_dim, n_kv_heads, batch_size=1):
        self.n_kv_heads = n_kv_heads
        self.head_dim = head_dim
        self.batch_size = batch_size
        self.keys = None
        self.values = None
        self.offset = 0
        self.step = 256

    def update_and_fetch(self, keys, values):
        prev = self.offset
        if self.keys is None or (prev + keys.shape[2]) > self.keys.shape[2]:
            n_steps = (self.step + keys.shape[2] - 1) // self.step
            shape = (self.batch_size, self.n_kv_heads, n_steps * self.step, self.head_dim)
            new_k = mx.zeros(shape, keys.dtype)
            new_v = mx.zeros(shape, values.dtype)
            if self.keys is not None:
                if prev % self.step != 0:
                    self.keys = self.keys[..., :prev, :]
                    self.values = self.values[..., :prev, :]
                self.keys = mx.concatenate([self.keys, new_k], axis=2)
                self.values = mx.concatenate([self.values, new_v], axis=2)
            else:
                self.keys, self.values = new_k, new_v

        self.offset += keys.shape[2]
        self.keys[..., prev : self.offset, :] = keys
        self.values[..., prev : self.offset, :] = values
        return self.keys[..., : self.offset, :], self.values[..., : self.offset, :]
    

def top_p_sampling(logits: mx.array, top_p: float, temperature: float, axis: int = -1) -> mx.array:
    """
    Apply top-p (nucleus) sampling to logits.

    Args:
        logits: The logits from the model's output.
        top_p: The cumulative probability threshold for top-p filtering.
        temperature: Temperature parameter for softmax distribution reshaping.
    Returns:
        token selected based on the top-p criterion.
    """
    # Apply temperature and compute softmax
    probs = mx.softmax(logits / temperature, axis=axis)
    
    # Sort probs in descending order
    sorted_indices = mx.argsort(-probs, axis=axis)
    sorted_probs = mx.take_along_axis(probs, sorted_indices, axis=axis)
    
    # Compute cumulative probabilities
    cumulative_probs = mx.cumsum(sorted_probs, axis=axis)
    
    # Create a mask for probs above the threshold
    mask = cumulative_probs <= top_p
    
    # Apply the mask to the sorted probabilities
    masked_probs = sorted_probs * mask
    
    # Normalize the masked probabilities
    normalized_probs = masked_probs / mx.sum(masked_probs, axis=axis, keepdims=True)
    
    # Sample from the normalized probabilities
    sampled_indices = mx.random.categorical(mx.log(normalized_probs), axis=axis)
    
    # Gather the original token indices
    tokens = mx.take_along_axis(sorted_indices, mx.expand_dims(sampled_indices, axis=axis), axis=axis)
    
    return tokens #.squeeze(axis=axis)


def generate_step(
    prompts: mx.array,
    model: nn.Module,
    temp: float = 0.0,
    repetition_penalty: Optional[float] = None,
    repetition_context_size: Optional[int] = 20,
    top_p: float = 1.0,
    logit_bias: Optional[Dict[int, float]] = None,
) -> Generator[Tuple[mx.array, mx.array], None, None]:
    """
    A generator producing token ids based on the given prompt from the model.

    Args:
        prompt (mx.array): The input prompt.
        model (nn.Module): The model to use for generation.
        temp (float): The temperature for sampling, if 0 the argmax is used.
          Default: ``0``.
        repetition_penalty (float, optional): The penalty factor for repeating
          tokens.
        repetition_context_size (int, optional): The number of tokens to
          consider for repetition penalty. Default: ``20``.
        top_p (float, optional): Nulceus sampling, higher means model considers
          more less likely words.

    Yields:
        Generator[Tuple[mx.array, mx.array]]: A generator producing
        one token and probability per call.
    """

    def sample(logits: mx.array) -> Tuple[mx.array, float]:
        if logit_bias:
            indices = mx.array(list(logit_bias.keys()))
            values = mx.array(list(logit_bias.values()))
            logits[:, indices] += values
        softmax_logits = mx.softmax(logits, axis=-1)

        if temp == 0:
            tokens = mx.argmax(logits, axis=-1, keepdims=True)
        else:
            if top_p > 0 and top_p < 1.0:
                tokens = top_p_sampling(logits, top_p, temp)
            else:
                scaled_logits = logits * (1 / temp)
                tokens = mx.random.categorical(logits * (1 / temp), axis=-1)
                if scaled_logits.ndim > 1:
                    tokens = mx.expand_dims(tokens, axis=-1)

        probs = softmax_logits[0, tokens]
        return tokens, probs

    if repetition_penalty:
        raise NotImplementedError("repetition_penalty not supported.")

    if repetition_penalty and (
        repetition_penalty < 0 or not isinstance(repetition_penalty, float)
    ):
        raise ValueError(
            f"repetition_penalty must be a non-negative float, got {repetition_penalty}"
        )

    # (bs, ntoks)
    y = prompts
    kv_heads = (
        [model.n_kv_heads] * len(model.layers)
        if isinstance(model.n_kv_heads, int)
        else model.n_kv_heads
    )

    cache = [BatchedKVCache(model.head_dim, n, y.shape[0]) for n in kv_heads]

    repetition_context = prompts

    if repetition_context_size and repetition_penalty:
        repetition_context = repetition_context[:,-repetition_context_size:]

    def _step(y):
        nonlocal repetition_context
        logits = model(y, cache=cache)
        logits = logits[:, -1, :]

        if repetition_penalty:
            logits = apply_repetition_penalty(
                logits, repetition_context, repetition_penalty
            )
            y, probs = sample(logits)
            repetition_context = mx.concatenate([repetition_context, y])
        else:
            y, probs = sample(logits)

        if repetition_context_size:
            if repetition_context.shape[1] > repetition_context_size:
                repetition_context = repetition_context[:,-repetition_context_size:]
        return y, probs

    y, p = _step(y)
    mx.async_eval(y)
    while True:
        next_y, next_p = _step(y)
        mx.async_eval(next_y)
        mx.eval(y)
        yield y, p
        y, p = next_y, next_p

def batch_generate(
    model,
    tokenizer,
    prompts: List[str],
    max_tokens: int = 100,
    verbose: bool = False,
    format_prompts: bool = True,
    formatter: Optional[Callable] = None,
    **kwargs,
) -> Union[str, Generator[str, None, None]]:
    """
    Generate a complete response from the model.

    Args:
       model (nn.Module): The language model.
       tokenizer (PreTrainedTokenizer): The tokenizer.
       prompt (str): The string prompt.
       max_tokens (int): The maximum number of tokens. Default: ``100``.
       verbose (bool): If ``True``, print tokens and timing information.
           Default: ``False``.
       formatter (Optional[Callable]): A function which takes a token and a
           probability and displays it.
       kwargs: The remaining options get passed to :func:`generate_step`.
          See :func:`generate_step` for more details.
    """
    if not isinstance(tokenizer, TokenizerWrapper):
        tokenizer = TokenizerWrapper(tokenizer)

    if verbose:
        print("=" * 10)
    
    if format_prompts:
        prompts_fm = [[{"role": "user", "content": prompt}] for prompt in prompts]
        prompts_fm = [tokenizer.apply_chat_template(prompt, add_generation_prompt=True, tokenize=False) for prompt in prompts_fm]
    else:
        prompts_fm = prompts

    # left-padding for batched generation
    tokenizer._tokenizer.padding_side = 'left'
    if tokenizer.pad_token is None:
        tokenizer._tokenizer.pad_token = tokenizer.eos_token
        tokenizer._tokenizer.pad_token_id = tokenizer.eos_token_id

    prompts_toks = mx.array(tokenizer._tokenizer(prompts_fm, padding=True)['input_ids'])
    tic = time.perf_counter()

    output_toks = []
    for (tokens, _), n in zip(
        generate_step(prompts_toks, model, **kwargs),
        range(max_tokens),
    ): 
        if n == 0:
            prompt_time = time.perf_counter() - tic
            tic = time.perf_counter()
        output_toks.append(tokens)
    output_toks = mx.concatenate(output_toks, axis=1)

    responses = [response.split(tokenizer.eos_token)[0].split(tokenizer.pad_token)[0] for response in tokenizer.batch_decode(output_toks.tolist())]
    if verbose:
        gen_time = time.perf_counter() - tic
        prompt_tps = prompts_toks.size / prompt_time
        gen_tps = output_toks.size / gen_time
        print(f"Prompt: {prompt_tps:.3f} tokens-per-sec")
        print(f"Generation: {gen_tps:.3f} tokens-per-sec")
        for prompt, response in zip(prompts, responses):
            print("=" * 10)
            print("Prompt:", prompt)
            print(response)
            
    return responses

# maxplotlib

custom_maxplotlib_error_plot_script = """import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(figsize=(10, 6))
background_color = "#f8f9fa"
text_color = "#e63946"
box_color = "#457b9d"
highlight_color = "#f1faee"
fig.patch.set_facecolor(background_color)
ax.set_facecolor(background_color)
ax.axis('off')
box = plt.Rectangle((0.1, 0.4), 0.8, 0.2, color=box_color, ec='none', alpha=0.5)
ax.add_patch(box)
error_message = "yeesh something went wrong"
ax.text(0.5, 0.5, error_message, ha='center', va='center', fontsize=24, color=highlight_color, fontweight='bold')
num_stars = 20
stars_x = np.random.uniform(0, 1, num_stars)
stars_y = np.random.uniform(0, 1, num_stars)
ax.scatter(stars_x, stars_y, s=100, color=highlight_color, edgecolor=text_color, linewidth=0.5, alpha=0.7, marker='*')
num_circles = 10
circles_x = np.random.uniform(0, 1, num_circles)
circles_y = np.random.uniform(0, 1, num_circles)
ax.scatter(circles_x, circles_y, s=500, color='none', edgecolor=box_color, linewidth=2, alpha=0.3)
for i in range(5):
    x = np.random.uniform(0.2, 0.8)
    y = np.random.uniform(0.2, 0.8)
    length = np.random.uniform(0.1, 0.3)
    ax.plot([x, x+length], [y, y+length], color=text_color, linewidth=2, alpha=0.5)
plt.title("maxplotlib error :) sorry", fontsize=30, color=text_color, fontweight='heavy', pad=20)
plt.show()"""

def ideas_to_python_scripts(
    ideas: List[str], 
    max_tokens: int = 3000,
    temp: float = 0.0
) -> List[str]:
    """
    Convert the prompts into matplotlib scripts

    Args:
        ideas (List[str]): prompts to generate python code (run in parallel)
        max_tokens (int): max_tokens
    """
    prompts = [matplotlib_numpy_prompt_template.format(user_message=idea) for idea in ideas]
    responses = batch_generate(model, tokenizer, prompts=prompts, max_tokens=max_tokens, verbose=True, temp=temp)
    res = []
    for r in responses:
        if ipython_start_tag in r and ipython_end_tag in r and "plt.show()" in r:
            python_code_start_index = r.find(ipython_start_tag) + len(ipython_start_tag)
            python_code_end_index = r.find(ipython_end_tag, python_code_start_index)
            python_code = r[python_code_start_index:python_code_end_index].strip()
        # elif "```python" in r and "plt.show()" in r:
        #     python_code_start_index = r.find("```python") + len("```python")
        #     python_code_end_index = r.find("```", python_code_start_index)
        #     python_code = r[python_code_start_index:python_code_end_index].strip()
        else: # error message plot
            python_code = custom_maxplotlib_error_plot_script
        res.append(python_code)
    return res


def run(
    user_message: str,
    num_ideas: int = 2
) -> str:
    """
    Convert the user message into multiple options for matplotlib-image-generating scripts

    Args:
        user_message (str): prompt
        max_tokens (int): max_tokens
        num_parallel (int): number of parallel LLM workers
    """
    idea_prompt = brainstorm_matplotlib_template.format(user_message=user_message, num_ideas=num_ideas)
    ideas = generate(
        model, tokenizer, 
        prompt=idea_prompt, temp=0.7,
        verbose=True, max_tokens=50*num_ideas)
    ideas = [x for x in ideas.split("IDEAS:")[1].strip().split("* idea") if x]
    print(len(ideas), "ideas:", ideas)
    return ideas_to_python_scripts(ideas)

def exec_matplotlib(python_code: str) -> Image:
    """
    Execute the input string as python code that produces an image with matplotlib

    Args:
        python_code (str): python script w/ matplotlib (& possibly numpy) code
    """
    plt.figure()
    local_vars = {'plt': plt, 'np': np}
    exec(python_code, local_vars, local_vars)
    plt.show()
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    plt.close()
    return Image.open(buf)

def image_to_base64(image):
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')

def get_images(matplotlib_scripts: List[str]):
    res = []
    for s in matplotlib_scripts:
        try:
            res.append(image_to_base64(exec_matplotlib(s)))
        except Exception as e:
            res.append(image_to_base64(exec_matplotlib(custom_maxplotlib_error_plot_script)))
    return res