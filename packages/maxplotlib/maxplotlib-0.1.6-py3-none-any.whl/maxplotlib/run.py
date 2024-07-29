import base64
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mlx_lm import generate
import numpy as np
from PIL import Image
from typing import List

from .llm import batch_generate, model, tokenizer

# llama 3.1 info from meta prompt guide
# https://llama.meta.com/docs/model-cards-and-prompt-formats/llama3_1

brainstorm_matplotlib_template = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Cutting Knowledge Date: December 2023
Today Date: 23 Jul 2024

You turn a user request into incredible ideas for visualizations.
You focus on clarity of the idea & success of implementation above all else.
You only come up with ideas for 2D matplotlib visualizations.
You always respond with {num_ideas} ideas like this:
IDEAS:
* idea 1 * first idea
...
* idea {num_ideas} * last idea

Your ideas are short but contain HELPFUL PLOTTING DETAILS.
You generate only ideas, no code<|eot_id|><|start_header_id|>user<|end_header_id|>

{user_message}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""

matplotlib_numpy_prompt_template = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython

Cutting Knowledge Date: December 2023
Today Date: 23 Jul 2024

# Tool Instructions
- You only import matplotlib, numpy, and standard python libraries that need no installation
- All figures need to have titles, and each subplot needs a title & axis labels<|eot_id|>
<|start_header_id|>user<|end_header_id|>

{user_message}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""

# return a 404 plot if we error out during generation

custom_maxplotlib_error_plot_script = """import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(figsize=(10, 6))
colors = {"bg": "#f8f9fa", "text": "#e63946", "box": "#457b9d", "highlight": "#f1faee"}
fig.patch.set_facecolor(colors["bg"])
ax.set_facecolor(colors["bg"])
ax.axis('off')
ax.add_patch(plt.Rectangle((0.1, 0.4), 0.8, 0.2, color=colors["box"], ec='none', alpha=0.5))
ax.text(0.5, 0.5, "yeesh something went wrong", ha='center', va='center', fontsize=24, color=colors["highlight"], fontweight='bold')
for shape, num, size, edge, fill in [('*', 20, 100, colors["text"], colors["highlight"]), ('o', 10, 500, colors["box"], 'none')]:
    ax.scatter(np.random.uniform(0, 1, num), np.random.uniform(0, 1, num), s=size, color=fill, edgecolor=edge, linewidth=0.5 if shape == '*' else 2, alpha=0.7 if shape == '*' else 0.3, marker=shape)
for _ in range(5):
    x, y, length = np.random.uniform(0.2, 0.8), np.random.uniform(0.2, 0.8), np.random.uniform(0.1, 0.3)
    ax.plot([x, x+length], [y, y+length], color=colors["text"], linewidth=2, alpha=0.5)
plt.title("maxplotlib error :) sorry", fontsize=30, color=colors["text"], fontweight='heavy', pad=20)
plt.show()"""


def user_message_to_python_scripts(
    user_message: str,
    num_ideas: int = 4,
    max_idea_tokens: int = 100,
    idea_temp: float = 0.2,
    max_script_tokens: int = 1000,
    script_temp: float = 0.0
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
        prompt=idea_prompt, temp=idea_temp,
        verbose=True, max_tokens=max_idea_tokens*num_ideas)
    ideas = [x for x in ideas.split("IDEAS:")[1].strip().split("* idea") if x]
    print(len(ideas), "ideas:", ideas)
    if len(ideas) > num_ideas:
        print("truncating")
        ideas = ideas[:num_ideas]
    prompts = [matplotlib_numpy_prompt_template.format(user_message=idea) for idea in ideas]
    responses = batch_generate(model, tokenizer, prompts=prompts, max_tokens=max_script_tokens, verbose=True, temp=script_temp)
    res = []
    for r in responses:
        if "<|python_tag|>" in r and "<|eom_id|>" in r and "plt.show()" in r:
            print("PARSING PYTHON TAG")
            python_code_start_index = r.find("<|python_tag|>") + len("<|python_tag|>")
            python_code_end_index = r.find("<|eom_id|>", python_code_start_index)
            python_code = r[python_code_start_index:python_code_end_index].strip()
        elif "```python" in r and "plt.show()" in r:
            print("PARSING PYTHON MARKDOWN")
            python_code_start_index = r.find("```python") + len("```python")
            python_code_end_index = r.find("```", python_code_start_index)
            python_code = r[python_code_start_index:python_code_end_index].strip()
        else: # error message plot
            print("!!! NO PARSING PYTHON")
            python_code = custom_maxplotlib_error_plot_script
        res.append(python_code)
    return res

def matplotlib_script_to_image(python_code: str) -> Image:
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

def python_scripts_to_images(matplotlib_scripts: List[str]):
    res = []
    for s in matplotlib_scripts:
        try:
            res.append(image_to_base64(matplotlib_script_to_image(s)))
        except Exception as e:
            print("~!~!~! PYTHON ERROR")
            res.append(image_to_base64(matplotlib_script_to_image(custom_maxplotlib_error_plot_script)))
    return res