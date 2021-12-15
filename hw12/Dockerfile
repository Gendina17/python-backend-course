FROM python:3.10-alpine

LABEL Author="Ninel"

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade pip

RUN apk add --no-cache postgresql-libs
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN python3 -m pip install -r requirements.txt --no-cache-dir
RUN apk --purge del .build-deps

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN python -m pip install psycopg2-binary
RUN pip install -r requirements.txt

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN adduser -D user

USER user