#!/bin/bash
sudo apt-get -y update
sudo apt-get -y install python3-pip python-dev python3-dev nginx
sudo export LC_ALL=C
pip install gunicorn flask
