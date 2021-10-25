# OCR service

### Architecture

![workflow](https://github.com/vangorade/OCR_async_service/blob/master/OCR/Workflow.png)

### Built With
* python
* Celery and Redis
* FastAPI

### Steps :
1. cd to OCR folder
```sh
$ cd OCR
```

2. Build image and spin docker container with number of workers
```sh
$ docker-compose -f docker-compose.yml up --build --scale worker=3
```

3. Trigger new task. 
```sh
$ (echo -n '{"base64str": "'; base64 project/temp/testocr.png; echo '"}') | curl -X POST -H "Content-Type: application/json" -d @- localhost:8004/predict
```

4. Use task_id from response to get OCR text. 
```sh
$ curl localhost:8004/predict/<task_id>
```

5. Monitor using Flower
```sh
$ http://localhost:5556 

```


