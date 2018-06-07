FROM python:3.6-alpine

ENV APP_HOME /app

WORKDIR $APP_HOME
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
ENV FLASK_APP server.py