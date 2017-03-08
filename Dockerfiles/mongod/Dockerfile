FROM ubuntu:16.04


COPY sources.list /etc/apt/sources.list
COPY resolv.conf /etc/resolv.conf

# Installation:
# Import mongoDB public GPG key AND create a mongoDB list file
# following the instructions from:
# https://docs.mongodb.com/manual/tutorial/install-mongodb-enterprise-on-ubuntu/
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
RUN echo "deb [ arch=amd64,arm64,ppc64el,s390x ] http://repo.mongodb.com/apt/ubuntu xenial/mongodb-enterprise/3.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-enterprise.list

# Update apt source AND install mongoDB
RUN apt update && apt install -y mongodb-enterprise

RUN apt clean && apt autoclean && apt autoremove -y

# Create the mongoDB data directory
RUN mkdir -p /data/db


# Set /usr/bin/mongod as the dockerized entry-point application
ENTRYPOINT ["/usr/bin/mongod"]