from ftplib import FTP
import ftplib
import os
import time

from celery import Celery
from dotenv import load_dotenv
from fastapi import Form
from img_processing import image_optimizer
from upload_ftp import placeFiles


load_dotenv(".env")

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")


ftp = FTP()
ftp.connect( '192.168.11.105', 20001)
ftp.login( 'ftpuser', 'user2022')


@celery.task(name="upload_folder_to_ftp_server")
def upload_task(task_upload: str= Form(...)):
    print('upload task:',task_upload)
    placeFiles(ftp, task_upload)
    time.sleep(int(10))
    return True


@celery.task(name="image_optimizer_task")
def image_optimizer_task(image: str = Form(...)):
    print('image:',image)
    image_optimizer(image) 
    return True