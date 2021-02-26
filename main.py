import shutil
from typing import List
from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.post('/')
async def root(file: UploadFile = File(...)):
    with open(f'{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {'file_name': file.filename}


@app.post('/img')
async def root(files: List[UploadFile] = File(...)):
    for image in files:
        with open(f'{image.filename}', 'wb') as buffer:
            shutil.copyfileobj(image.file, buffer)

    return {'file_name': 'good'}
