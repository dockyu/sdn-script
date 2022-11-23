#!/bin/bash

sudo mn --mac --switch ovsk,protocols=OpenFlow13 --controller remote,ip=127.0.0.1,port=6653 --arp