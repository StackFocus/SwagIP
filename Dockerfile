FROM ubuntu:latest
MAINTAINER Swagger.pro

RUN mkdir -p /opt/swagip/git
COPY ./ /opt/swagip/git
RUN apt-get update && apt-get install -y \
    python-dev \
    python-virtualenv \
    python-pip
RUN virtualenv /opt/swagip/env

RUN . /opt/swagip/env/bin/activate && pip install -r /opt/swagip/git/requirements.txt

#Probably some supervisor stuff eventually to run some wsgi to run the flask program
