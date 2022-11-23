#!/bin/bash

sudo mn --controller remote,ip=192.168.98.128,port=6653 --switch=ovsk,protocols=OpenFlow13 --custom $1 --topo=mytopo

