#!/usr/bin/env bash

set -x
set -ueo pipefail

cd /home/ubuntu/pseudotest/test_django

apt-get update
apt-get install -y nginx default-libmysqlclient-dev python3-pip

if ! [[ -d /etc/nginx/sites-available ]]; then
    mkdir /etc/nginx/sites-available 
fi

if ! [[ -d /etc/nginx/sites-enabled ]]; then
    mkdir /etc/nginx/sites-enabled
fi

pip3 install -r requirements.txt