FROM python:3.11-slim

WORKDIR /app

LABEL maintainer="mdanarul7075@gmail.com"
LABEL description="Development Image School Management"

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat-traditional gcc postgresql \
    && apt-get clean

RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin python3-gdal python3-gdal \
    xvfb

RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app