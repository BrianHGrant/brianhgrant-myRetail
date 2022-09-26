# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

ARG requirements

WORKDIR /app

COPY $requirements requirements.txt
RUN pip3 install -qr requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
