#!/usr/bin/env bash

cd /home/ubuntu/pseudotest/test_django

sudo apt-get update
sudo apt-get install -y nginx
pip3 install -r requirements.txt