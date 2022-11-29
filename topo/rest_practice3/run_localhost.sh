#!/bin/bash

if [ -z "$1" ]; then
    topo=rest_topo3.py
else
    topo=$1
fi

sudo mn --controller remote,ip=127.0.0.1,port=6653 --switch=ovsk,protocols=OpenFlow13 --custom $topo --topo=mytopo

