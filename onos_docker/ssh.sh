#!/bin/bash

echo "password:karaf"

ssh -p 8101 karaf@127.0.0.1 -o "UserKnownHostsFile=/dev/null"
