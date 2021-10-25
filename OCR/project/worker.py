import os
import time
import io
from PIL import Image, ImageFile
from celery import Celery
from utils import read_image, base64str_to_PILImage
ImageFile.LOAD_TRUNCATED_IMAGES = True

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get(
    "CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get(
    "CELERY_RESULT_BACKEND", "redis://localhost:6379")


@celery.task(name="create_task")
def create_task(task_type):
    try:
        time.sleep(int(task_type) * 10)
        return True
    except Exception as e:
        print(e)
        return False


@celery.task(name="OCR")
def task_OCR(image_data):
    try:
        image = base64str_to_PILImage(image_data)
        image = image.convert('1')
        text = read_image(image)
        return text
    except Exception as e:
        print(e)
        return False
