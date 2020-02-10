#!/bin/bash

while :
do
  if ping -c 1 ip_address &> /dev/null
  then
    echo "Host is online"
    break
  fi
  sleep 5
done
