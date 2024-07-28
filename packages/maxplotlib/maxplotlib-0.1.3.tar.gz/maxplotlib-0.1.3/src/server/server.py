from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from time import time

from maxplotlib.run import run, get_images

app = FastAPI(debug=False)

def validate_user_input(user_input: str, max_user_input_chars: int = 2000) -> str:
    if len(user_input) > max_user_input_chars:
        raise ValueError(f"Input is {len(user_input)} chars, maximum is {max_user_input_chars} characters.")
    return user_input

    
@app.post("/plot/")
async def plot_api(prompt: str = Form(...)):
    prompt = validate_user_input(prompt)
    matplotlib_scripts = run(prompt)
    images = get_images(matplotlib_scripts)
    return JSONResponse(content={"timestamp": time(), "prompt": prompt, "python_scripts": matplotlib_scripts, "images": images})