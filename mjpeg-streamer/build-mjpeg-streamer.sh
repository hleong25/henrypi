#!/bin/sh

git clone https://github.com/jacksonliam/mjpg-streamer
cd mjpg-streamer/mjpg-streamer-experimental
make
checkinstall --pkgversion=0.0.1
ln -s /mjpg-streamer/mjpg-streamer-experimental/mjpg-streamer_*.deb /
