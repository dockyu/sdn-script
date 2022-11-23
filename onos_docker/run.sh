#!/bin/bash

docker run --rm -d --name onos -p 6640:6640 -p 6653:6653 -p 8101:8101 -p 8181:8181 -p 9876:9876  onosproject/onos:2.7-latest
