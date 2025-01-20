FROM ubuntu:22.04

## information about this image ##
LABEL maintainer="james"
LABEL version="1.0"
LABEL description="2025 winter web image"

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive

## create folder to store data of web ##
RUN mkdir /app
WORKDIR /app
COPY . .

## install tmux ##
RUN apt-get update && apt-get install -y wget
RUN apt update && apt install -y tmux

## package for postgresql python package ##
RUN apt install libpq-dev python3-dev -y
RUN apt install build-essential -y

## download brew and install ta-lib##
# RUN apt-get install build-essential
RUN apt install git -y && apt install curl -y && apt install vim -y
#RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
#RUN eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
#ENV PATH="/home/linuxbrew/.linuxbrew/bin:/home/linuxbrew/.linuxbrew/sbin:${PATH}"
#RUN brew install ta-lib


## miniconda ##
#change sh base on your system
WORKDIR /
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh && \
    bash Miniconda3-latest-Linux-aarch64.sh -b -p /opt/conda && \
    rm Miniconda3-latest-Linux-aarch64.sh
ENV PATH=/opt/conda/bin:$PATH
RUN /opt/conda/bin/conda init bash

## postgresql ##
RUN apt install postgresql postgresql-contrib -y


WORKDIR /app


## after get into container ##

## adding new user in postgresql
# service postgresql start
# su postgres 
# psql
# CREATE USER userandrew WITH PASSWORD '123';
## CREATE USER test WITH PASSWORD 'mypassword';
# CREATE DATABASE andrewdata OWNER userandrew;
## CREATE DATABASE mydb OWNER test;
# GRANT ALL PRIVILEGES ON DATABASE andrewdata TO userandrew;
## GRANT ALL PRIVILEGES ON DATABASE mydb TO test;
# exit

## modify common/usersetting.py and stock/common/usersetting.py

## create virtual environment ##
# conda create -n lab_training python=3.9.6 -y && conda activate lab_training && pip install -r Lab_Training/requirement_Lab_training.txt && conda install -c conda-forge ta-lib && conda deactivate
# conda create -n accounts python=3.9.6 -y && conda activate accounts && pip install -r accounts/requirements.txt && conda deactivate

# -------------------del------------------------ #
# conda create -n func_api python=3.9.6 -y && conda activate func_api && pip install -r func_api/requirements.txt && conda deactivate
# -------------------del------------------------ #

## start server ##
# tmux
# cd /web_folder/Lab_Training/
# conda activate lab_training
# python manage.py runserver 0.0.0.0:8000
# ctrl + b +d

# tmux
# cd /web_folder/accounts/
# conda activate accounts
# python manage.py migrate
# python manage.py runserver 127.0.0.1:8081
# ctrl + b +d

# -------------------del------------------------ #
# tmux
# cd /web_folder/func_api/
# conda activate func_api
# python manage.py runserver 127.0.0.1:8080
# ctrl + b +d
# -------------------del------------------------ #
