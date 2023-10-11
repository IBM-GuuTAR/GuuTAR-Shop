FROM node:18-alpine as build-stage

RUN mkdir /usr/app

COPY . /usr/app

WORKDIR /usr/app

RUN npm install

ENV PATH /usr/src/app/node_modules/.bin:$PATH

RUN npm run build

FROM nginx:alpine

WORKDIR /usr/share/nginx/html

RUN rm -rf ./*

COPY --from=build-stage /usr/app/build .

COPY ./nginx/monitor-able.conf /etc/nginx/conf.d/monitor-able.conf

ENTRYPOINT ["nginx", "-g", "daemon off;"]