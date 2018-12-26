# docker-nginx-proxy
Nginx configuration to reverse proxy the others missiles

# Install

You need docker, with docker-compose.

Create the `certs` directory
```shell
mkdir certs
```

Create the docker network:
```shell
docker network create nginx-proxy
```

Missiles `docker-compose.yml` file should follow the format:
```
version: "3"
services:
  nginx:
    image: nginx
    restart: always
    environment:
      - VIRTUAL_HOST=mysite.example.com
      - LETSENCRYPT_HOST=mysite.example.com
      - LETSENCRYPT_EMAIL=email@example.com
    volumes:
      - ./:/usr/share/nginx/html
networks:
  default:
    external:
      name: nginx-proxy
```
