#!/bin/sh

docker login

docker buildx build --platform=linux/amd64,linux/arm64 -t hleong25/henrypi-nginx --push .
docker buildx build --platform=linux/amd64,linux/arm64 -t hleong25/henrypi-nginx:alpine --file Dockerfile.alpine --push .
