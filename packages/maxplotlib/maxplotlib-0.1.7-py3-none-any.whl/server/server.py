from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from time import time

from maxplotlib.run import user_message_to_python_scripts, python_scripts_to_images

app = FastAPI(debug=False)

def validate_user_input(user_input: str, max_user_input_chars: int = 2000) -> str:
    if len(user_input) > max_user_input_chars:
        raise ValueError(f"Input is {len(user_input)} chars, maximum is {max_user_input_chars} characters.")
    return user_input
    
@app.post("/plot/")
async def plot_api(prompt: str = Form(...)):
    prompt = validate_user_input(prompt)
    matplotlib_scripts, captions = user_message_to_python_scripts(prompt)
    images = python_scripts_to_images(matplotlib_scripts, captions)
    return JSONResponse(content={"timestamp": time(), "prompt": prompt, "python_scripts": matplotlib_scripts, "images": images})