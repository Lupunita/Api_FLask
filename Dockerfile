FROM postgres:latest

ENV POSTGRES_PASSWORD=securepassword

COPY init.sql /docker-entrypoint-initdb.d/


WORKDIR /usr/lib/app
COPY ./Container .


ENV APP_SETTINGS="config.DevelopmentConfig"
ENV DB_USERNAME='postgres'
ENV DB_PASSWORD='securepassword'
ENV DB_HOST='0.0.0.0'
ENV DB_PORT='5432'
ENV FLASK_ENV='development'
ENV FLASK_APP='.'
ENV SECRET_KEY='wFwb4353GFuLF2U1vc3MgaXMgYSBo2'
ENV DB_NAME='testovacka'

RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get install -y git
RUN pip3 install -r requirements.txt;

EXPOSE 5000/tcp

    