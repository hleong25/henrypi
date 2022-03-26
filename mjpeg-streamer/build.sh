#!/bin/sh

docker login

docker buildx build --platform=linux/amd64 -t hleong25/mjpeg-streamer:amd64 --push .
docker buildx build --platform=linux/arm64 -t hleong25/mjpeg-streamer:arm64 --push .
