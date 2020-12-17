FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 python3-pip

RUN mkdir /usr/src/app

COPY . /usr/src/app/

RUN cd /usr/src/app/ && pip3 install -r requirements.txt

WORKDIR /usr/src/app/