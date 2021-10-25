# pull official base image
FROM python:3.9.5-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

RUN apt-get -y update && apt-get install -y tesseract-ocr && apt-get install -y libtesseract-dev

COPY ./requirements.txt .
RUN pip install -r requirements.txt


# COPY ./test.jpg /usr/src/app/test.jpg
# copy project
COPY . .
