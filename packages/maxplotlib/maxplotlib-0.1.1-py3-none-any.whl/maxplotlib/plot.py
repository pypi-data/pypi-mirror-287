from contextlib import redirect_stdout
import io
import matplotlib.pyplot as plt
import numpy as np
from mlx_lm import load, generate
from PIL import Image

model, tokenizer = load("mlx-community/Meta-Llama-3.1-70B-Instruct-4bit")

def plot(user_message: str) -> Image:

    prompt = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha

Cutting Knowledge Date: December 2023
Today Date: 23 Jul 2024

You are a helpful python plotting assistant. You always give a rich & descriptive title, labels, & context to your generated plots, charts, and graphs.<|eot_id|>
<|start_header_id|>user<|end_header_id|>

{user_message}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""

    response = generate(model, tokenizer, prompt=prompt, verbose=True, max_tokens=500)
    
    start_tag = '<|python_tag|>'
    end_tag = '<|eom_id|>'
    python_code_start_index = response.find(start_tag) + len(start_tag)
    python_code_end_index = response.find(end_tag, python_code_start_index)
    python_code = response[python_code_start_index:python_code_end_index].strip()
    import matplotlib
    matplotlib.use('Agg')
    plt.figure()
    f = io.StringIO()
    with redirect_stdout(f):
        local_vars = {'plt': plt, 'np': np}
        exec(python_code, local_vars, local_vars)
        plt.show()
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    plt.close()
    image = Image.open(buf)
    
    return image