FROM python:3.14-slim 
LABEL key="Advanced Blog"

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN apt-get update && apt-get install -y gettext
RUN pip3 install --upgrade pip && pip install -r requirements.txt

COPY ./core .