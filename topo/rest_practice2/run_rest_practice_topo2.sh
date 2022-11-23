#!/bin/bash

sudo mn --topo linear,2 --mac --switch ovsk,protocols=OpenFlow13 --controller remote,ip=127.0.0.1,port=6653 --arp