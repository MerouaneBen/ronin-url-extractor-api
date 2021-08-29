#----------------------------
# Celery-Base
# image of Celery worker
#----------------------------
# VERSION 0.0.1
# AUTHOR: Merouane Benthameur

FROM python:3.9-bullseye
LABEL authors="merouane.benth@gmail.com"

# Never prompts the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux


RUN mkdir /app
ENV CeleryHome='/app'
ENV C_FORCE_ROOT true

# copy scripts to Home
COPY . ${CeleryHome}/
WORKDIR ${CeleryHome}

# **********************************************
# If a specific locale is required, use the following commands (preferably in your docker child image)...
# By default, we set some environment variables to predefined C.UTF-8 locale
ENV LANG "C.UTF-8"
ENV LANGUAGE "C.UTF-8"
ENV LC_ALL "C.UTF-8"

# install nodejs
RUN apt-get update \
    && apt-get -y install curl libmariadb3 libmariadb-dev

# define timezone variable
ENV TZ=America/Montreal

# set timezone to Montreal TZ
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install dependecices
RUN pip3 install --no-cache-dir -r requirements.txt
