FROM node:alpine as builder

WORKDIR /app

COPY ./frontend/package.json .

RUN npm install

COPY ./frontend .

RUN npm run build

# ============================== #

FROM python:3.6

RUN apt-get update

RUN apt-get install vim -y

WORKDIR /app

RUN pip install --upgrade pip

COPY ./backend/requirements.txt .

RUN pip install -r requirements.txt

COPY ./backend .

COPY ./docker/entrypoint.sh ./docker/run.sh /

COPY --from=builder /app/dist /app/assets
