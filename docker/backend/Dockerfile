FROM python:3.6

RUN apt-get update

RUN apt-get install vim -y

WORKDIR /app

RUN pip install --upgrade pip

COPY ./backend/requirements.txt .

RUN pip install -r requirements.txt

COPY ./backend .

COPY ./run.sh .