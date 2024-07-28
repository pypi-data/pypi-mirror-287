import base64
from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse
from io import BytesIO
from maxplotlib.plot import plot
from time import time

app = FastAPI(debug=False)

def encode_image_to_base64(image):
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')

def stream_text_result(result, media_type="text/plain"):
    try:
        return StreamingResponse(result, media_type=media_type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/plot/")
async def plot_api(prompt: str = Form(...)):
    image = plot(prompt)
    encoded_image = encode_image_to_base64(image)
    return JSONResponse(content={"timestamp": time(), "prompt": prompt, "image": encoded_image})