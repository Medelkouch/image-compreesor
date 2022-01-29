from typing import List
from config import IMG_COMPRESS_PATH
from fastapi import FastAPI, HTTPException
from img_processing import image_optimizer, zip_folder
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from logger import log

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


class ImageBody(BaseModel):
    id: int
    name: str


class OptImgBody(BaseModel):
    folder_id: str
    images: List[ImageBody]


@app.post("/api/image/optimize")
def optimize_images(body: OptImgBody):
    optimized_images = []
    skipped_images = []

    images = body.images
    folder_id = str(body.folder_id) + "/"

    log.info(f">> Images processing start : {body}")
    for img in images:
        if image_optimizer(img, folder_id):
            optimized_images.append(img.id)
        else:
            skipped_images.append(img)

    log.info(f">> Processing done !")
    return {
        'optimized_images': optimized_images,
        # 'skipped_images': skipped_images
    }

#####################################################################


class DowImgBody(BaseModel):
    folder_id: str


@app.post("/api/image/download")
def download_images(body: DowImgBody):
    folder_path = IMG_COMPRESS_PATH + body.folder_id + '/'

    try:
        download = zip_folder(folder_path)
    except Exception as e:
        log.error(f"Exception msg: {e}")
        raise HTTPException(
            status_code=400, detail="Bad request download failed !")
    else:
        return download
