#!/bin/sh

cd henrypi-nginx
./build.sh

cd ../henrypi-api
./build.sh

cd ../henrypi-ui
./build.sh
