FROM node:alpine as builder

WORKDIR /app

COPY ./frontend/package.json .

RUN npm install

COPY ./frontend .

RUN npm run build

# ============================== #

FROM nginx:alpine

WORKDIR /app

RUN rm -rf /etc/nginx/conf.d/*

COPY ./docker/frontend/site.conf /etc/nginx/conf.d

COPY --from=builder /app/dist /app

CMD ["nginx", "-g", "daemon off;"]