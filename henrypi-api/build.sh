#!/bin/sh

docker login

docker buildx build --platform=linux/amd64,linux/arm64 -t hleong25/henrypi-api --push .
docker buildx build --platform=linux/amd64,linux/arm64 -t hleong25/henrypi-api:alpine3.14 --file Dockerfile.alpine --push .
