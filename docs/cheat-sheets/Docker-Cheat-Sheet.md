---
title: Docker Cheat Sheet
description: This cheat sheet should help you execute common Docker operations
status: published
tags:
 - docker
 - cheat sheet
date: 2023-06-15
---
# Docker Cheat Sheet

This cheat sheet should help you navigate and execute common Docker operations efficiently.

| Command | Description | Example |
| --- | --- | --- |
| `docker run` | Creates and starts a new container | `docker run -it ubuntu:latest` |
| `docker ps` | Lists all running containers | `docker ps` |
| `docker images` | Lists all available images | `docker images` |
| `docker pull` | Pulls an image from a registry | `docker pull nginx:latest` |
| `docker build` | Builds an image from a Dockerfile | `docker build -t myimage .` |
| `docker start` | Starts one or more stopped containers | `docker start container_name` |
| `docker stop` | Stops one or more running containers | `docker stop container_name` |
| `docker restart` | Restarts a running container | `docker restart container_name` |
| `docker exec` | Runs a command inside a running container | `docker exec -it container_name bash` |
| `docker rm` | Removes one or more containers | `docker rm container_name` |
| `docker rmi` | Removes one or more images | `docker rmi image_name` |
| `docker logs` | Displays the logs of a container | `docker logs container_name` |
| `docker cp` | Copies files/folders between a container and the host | `docker cp container_name:/path/to/file .` |
| `docker network` | Manages Docker networks | `docker network create mynetwork` |
| `docker volume` | Manages Docker volumes | `docker volume create myvolume` |
| `docker-compose up` | Starts containers defined in a Compose file | `docker-compose up -d` |

Remember to replace `container_name`, `image_name`, and other placeholders with actual names relevant to your setup.