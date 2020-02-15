FROM python:3.7-alpine
MAINTAINER Edward Cho

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

#Security purpose, use separate user from root account
RUN adduser -D user
USER user