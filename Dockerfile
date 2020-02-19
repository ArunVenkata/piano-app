FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update && apt-get install -y ffmpeg
RUN mkdir piano-app
WORKDIR /piano-app
ADD . /piano-app/
RUN pip install -r requirements.txt