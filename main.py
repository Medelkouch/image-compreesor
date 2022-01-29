from typing import List
from fastapi import FastAPI
from img_processing import image_optimizer
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
