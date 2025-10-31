FROM python:3.14-slim 
LABEL key="Advanced Blog"

ENV PYTHONNUNBUFFERED=1

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN pip3 install --upgrade pip && pip install -r requirements.txt

COPY ./core .