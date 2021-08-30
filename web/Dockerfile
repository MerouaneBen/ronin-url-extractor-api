#----------------------------
# image of api image
#----------------------------
# VERSION 0.0.1
# AUTHOR: Merouane Benthameur

FROM python:3.9-bullseye
LABEL authors="merouane.benth@gmail.com"

ARG VERSION=V0.0.0

# Never prompts the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

# define timezone variable
ENV TZ=America/Montreal

ENV LANG "C.UTF-8"
ENV LANGUAGE "C.UTF-8"
ENV LC_ALL "C.UTF-8"

RUN apt-get update -yqq \
    && apt-get install -yqq unzip \
    && apt-get install -y locales apt-utils curl vim python3-pymysql

COPY requirements.txt requirements.txt

# set timezone to Montreal TZ
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV API_VERSION = ${VERSION}

# default home for the web
ENV API_HOME=/home/flask/app/web
COPY . ${API_HOME}

# Create the group and user to be used in this container
RUN groupadd flaskgroup && useradd -m -g flaskgroup -s /bin/bash flask
RUN chown -R flask:flaskgroup /home/flask

# set the working directory
WORKDIR ${API_HOME}
COPY ./ ${API_HOME}/

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x boot.sh

USER root

ENTRYPOINT ["./boot.sh"]