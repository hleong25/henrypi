FROM debian:bullseye-slim

RUN apt update
RUN apt install -y cmake
RUN apt install -y libjpeg-dev
RUN apt install -y git
RUN apt install -y checkinstall

COPY ./build-mjpeg-streamer.sh /
RUN /build-mjpeg-streamer.sh
