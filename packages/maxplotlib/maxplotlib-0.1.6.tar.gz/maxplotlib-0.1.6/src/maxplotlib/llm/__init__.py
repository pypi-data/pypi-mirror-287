from mlx_lm import load
from .generation import batch_generate

model, tokenizer = load("mlx-community/Meta-Llama-3.1-8B-Instruct-8bit")