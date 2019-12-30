import os
import aiohttp
import asyncio
import uvicorn
import tensorflow as tf
import sys
from pathlib import Path
from tensorflow.keras.models import load_model
from suptools.tftools import central_crop, process_img_bytes
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles

# CONFIGURATIONS HERE
export_file_url = 'https://storage.googleapis.com/tf2-workshop-fundamental-rig-253009/model2.h5'
export_file_name = 'model2.h5'
classes = ['mee_goreng', 'chicken_rice', 'roti_prata']
valid_aug = [central_crop]


path = Path(__file__).parent
app = Starlette()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['X-Requested-With', 'Content-Type'])
app.mount('/static', StaticFiles(directory='app/static'))


async def download_file(url, dest):
    if dest.exists(): return
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open(dest, 'wb') as f:
                f.write(data)


async def setup_learner():
    await download_file(export_file_url, path/'models'/export_file_name)
    try:
        learn = load_model(str(path/'models'/export_file_name))
        return learn
    except RuntimeError as e:
            print(e)


loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(setup_learner())]
learn = loop.run_until_complete(asyncio.gather(*tasks))[0]
loop.close()


@app.route('/')
async def homepage(request):
    html_file = path / 'view' / 'index.html'
    return HTMLResponse(html_file.open().read())


@app.route('/analyze', methods=['POST'])
async def analyze(request):
    img_data = await request.form()
    img_bytes = await (img_data['file'].read())
    try:
        img = process_img_bytes(img_bytes, img_size=224, augments=valid_aug)
        label_arg = learn.predict(img, steps=1).argmax(axis=-1)[0]
        prediction = classes[label_arg]
    except Exception as e:
        prediction = str(e)
    return JSONResponse({'result': str(prediction)})


if __name__ == '__main__':
    if 'serve' in sys.argv:
        uvicorn.run(app=app, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), log_level="info")
