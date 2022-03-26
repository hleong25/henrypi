#!/bin/sh

docker login

# docker buildx build --platform=linux/amd64 -t hleong25/henrypi-api:amd64 --push .
# docker buildx build --platform=linux/arm64 -t hleong25/henrypi-api:arm64 --push .

docker buildx build --platform=linux/amd64,linux/arm64 -t hleong25/henrypi-api --push .
