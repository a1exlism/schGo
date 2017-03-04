FROM ubuntu:16.04

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak

COPY deploy/sources.list /etc/apt/sources.list
COPY deploy/resolv.conf /etc/resolv.conf

# flask
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y python3-pip python3-dev build-essential

# Redis

# mongoDB

RUN apt-get autoclean -y && apt-get autoremove -y
