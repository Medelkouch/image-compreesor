import os
import time

from celery import Celery
from dotenv import load_dotenv
from fastapi import Form
from img_processing import image_optimizer

load_dotenv(".env")

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")


@celery.task(name="create_task")
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    print("hello task")
    return True


@celery.task(name="image_optimizer_task")
def image_optimizer_task(image: str = Form(...)):
    print('image:',image)
    image_optimizer(image)
    time.sleep(int(10))
    return True