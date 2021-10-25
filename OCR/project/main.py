from fastapi import Body, FastAPI, Form, Request, UploadFile, File
from fastapi.responses import JSONResponse
from worker import create_task, task_OCR
from typing import Dict
from data import Data
from celery.result import AsyncResult
from data import Data
app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tasks", status_code=201)
def test(payload=Body(...)) -> JSONResponse:
    task_type = payload["type"]
    task = create_task.delay(int(task_type))
    return JSONResponse({"task_id": task.id})


@app.post("/predict", status_code=201)
def predict(image: Data) -> JSONResponse:
    try:
        job = task_OCR.delay((image.base64str))
        return JSONResponse({"job_id": job.id})
    except Exception as e:
        return JSONResponse({"error": str(e)})


@app.get("/predict/{task_id}")
def predict_result(task_id) -> JSONResponse:
    try:
        job_result = AsyncResult(task_id)
        result = {
            "task_id": task_id,
            "task_status": job_result.status,
            "task_result": job_result.result,
        }
        return JSONResponse(result)
    except Exception as e:
        return JSONResponse({"error": str(e)})


@app.get("/tasks/{task_id}")
def test_result(task_id) -> JSONResponse:
    try:
        task_result = AsyncResult(task_id)
        result = {
            "task_id": task_id,
            "task_status": task_result.status,
            "task_result": task_result.result
        }
        return JSONResponse(result)
    except Exception as e:
        return JSONResponse({"error": str(e)})
