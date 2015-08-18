FROM ubuntu:latest
MAINTAINER Swagger.pro

RUN mkdir -p /opt/swagip/git && mkdir /opt/swagip/logs
COPY ./ /opt/swagip/git
VOLUME ["/opt/swagip/git"]
RUN apt-get update && apt-get install -y \
    python-dev \
    python-virtualenv \
    python-pip \
    supervisor

RUN virtualenv /opt/swagip/env

RUN . /opt/swagip/env/bin/activate && pip install -r /opt/swagip/git/requirements.txt

#Probably some supervisor stuff eventually to run some wsgi to run the flask program

EXPOSE 80

CMD /usr/bin/supervisord -c /opt/swagip/git/supervisord.conf   
