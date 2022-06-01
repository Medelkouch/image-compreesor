from typing import List
from config import IMG_COMPRESS_PATH, IMG_COMPRESS_REMOTE_PATH, ROOT_DIR_PATH
from fastapi import Body, FastAPI, HTTPException, Request, Form
from img_processing import image_optimizer, zip_folder
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from logger import log

from celery_worker import create_task, image_optimizer_task
from fastapi.responses import JSONResponse

# uvicorn main:app --host 0.0.0.0 --port 80 --reload

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"status": "Server working ..."}

#####################################################################
@app.post("/tasks", status_code=201)
def run_task(payload = Body(...)):
    task_type = payload["type"]
    task = create_task.delay(int(task_type))
    return JSONResponse({"task_id": task.id})

#####################################################################
@app.post("/api/compress_task", status_code=201)
def run_task(payload = Body(...)):
    image_link = payload["image"]
    task = image_optimizer_task.delay(str(image_link))
    return JSONResponse({"task_id": task.id})

#####################################################################


class ImageBody(BaseModel):
    id: int
    name: str


@app.post("/api/image/optimize")
def optimize_images(req: Request, image: str = Form(...)):
    optimized_images = []
    skipped_images = []

    log.info(f">> Images processing start : {image}")
    if image_optimizer(image):
        optimized_images.append('ok')
    else:
        skipped_images.append('error')

    log.info(f">> Processing done !")
    return {
        'content': image,
        'optimized_images': optimized_images,
        'skipped_images': skipped_images
    }

#####################################################################


class DowImgBody(BaseModel):
    estate_id: str


@app.post("/api/image/download")
def download_images(body: DowImgBody):
    print(body.estate_id, 'body')
    # folder_path = ROOT_DIR_PATH + body.estate_id + '/'
    folder_path = ROOT_DIR_PATH

    try:
        download = zip_folder(folder_path)
    except Exception as e:
        log.error(f"Exception msg: {e}")
        raise HTTPException(
            status_code=400, detail="Bad request download failed !")
    else:
        return download
