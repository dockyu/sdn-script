#!/bin/bash

sudo mn --controller remote,ip=127.0.0.1,port=6653 --switch=ovsk,protocols=OpenFlow13 --custom $1 --topo=mytopo

