#!/bin/bash

docker run -it --rm --privileged -e DISPLAY --name mininet -v /tmp/.X11-unix:/tmp/.X11-unix -v /lib/modules:/lib/modules buildandshipalan/mininet:v5
