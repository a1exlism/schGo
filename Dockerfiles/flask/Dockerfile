FROM ubuntu:16.04


RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak

ADD sources.list /etc/apt/sources.list
ADD resolv.conf /etc/resolv.conf
ADD ../../requirements.txt /app/

# flask
RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install  python3-pip python3-dev build-essential -y

# for cryptography
RUN apt install libssl-dev libffi-dev -y

RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt

RUN apt clean && apt-get autoclean && apt-get autoremove -y

ENV PYTHONPATH $PYTHONPATH:/app
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# 坑死
# ENTRYPOINT [/usr/bin/python3, /app/sgo/__init__.py]
