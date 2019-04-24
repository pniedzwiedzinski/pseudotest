#!/usr/bin/env bash

set -x
set -ueo pipefail

cd /home/ubuntu/pseudotest/test_django

sudo apt-get update
sudo apt-get install -y default-libmysqlclient-dev
pip3 install -r requirements.txt