FROM python:3.7-alpine
MAINTAINER Edward Cho

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
#Security purpose, use separate user from root account
RUN adduser -D user
RUN chown -R user:user /vol/
#Sets the ownership of /vol to user (-R is recursive)
RUN chmod -R 755 /vol/web
#THe user(owner) can do everything in the directory, the rest can read
USER user