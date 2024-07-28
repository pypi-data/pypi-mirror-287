from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
import re
from time import time
import unicodedata

from maxplotlib.run import run, get_images

app = FastAPI(debug=False)

allowed_chars_in_user_input = re.compile(r"^[a-zA-Z0-9,.!?(){}\[\]+\-*/%=:'\"_ ]+$")
max_user_input_chars = 500

def validate_user_input(user_input: str) -> str:
    user_input = unicodedata.normalize('NFC', user_input.strip())
    user_input = ''.join(char for char in user_input if char.isprintable())
    if not allowed_chars_in_user_input.match(user_input):
        violating_chars = set()
        for char in user_input:
            if not allowed_chars_in_user_input.match(char):
                violating_chars.add(char)
        raise ValueError(f"Invalid characters in user input: {violating_chars}")
    if len(user_input) > max_user_input_chars:
        raise ValueError(f"Input is {len(user_input)} chars, maximum is {max_user_input_chars} characters.")
    return user_input

    
@app.post("/plot/")
async def plot_api(prompt: str = Form(...)):
    prompt = validate_user_input(prompt)
    matplotlib_scripts = run(prompt)
    images = get_images(matplotlib_scripts)
    return JSONResponse(content={"timestamp": time(), "prompt": prompt, "python_scripts": matplotlib_scripts, "images": images})