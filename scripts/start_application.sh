#!/usr/bin/env bash

cd /home/ubuntu/pseudotest/test_django

DATE=$(date +%H-%M-%S-%d-%m-%Y)

mkdir /var/log/pseudotest
touch /var/log/pseudotest/${DATE}.log

gunicorn --pid gunicorn.pid --workers=2 --access-logfile /var/log/pseudotest/${DATE}.log -D test_django.wsgi -b 0.0.0.0:80