FROM ubuntu:14.04.4
MAINTAINER Swagger.pro

RUN mkdir -p /opt/swagip/git && mkdir /opt/swagip/logs
COPY ./ /opt/swagip/git
RUN apt-get update && apt-get install -y \
    python-dev \
    python-virtualenv \
    python-pip

RUN virtualenv /opt/swagip/env
RUN . /opt/swagip/env/bin/activate && pip install -r /opt/swagip/git/requirements.txt
WORKDIR /opt/swagip/git
EXPOSE 80
CMD /opt/swagip/env/bin/uwsgi --ini=/opt/swagip/git/wsgi.ini
