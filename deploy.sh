#!/bin/sh
RPI_HOST=rpi3
RPI_PATH='~/Workspace/nextbus/'
rsync -azP ./ $RPI_HOST:$RPI_PATH
