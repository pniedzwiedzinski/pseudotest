#!/usr/bin/env bash

set -x
set -ueo pipefail

cd /home/ubuntu/pseudotest/test_django

DATE=$(date +%H-%M-%S-%d-%m-%Y)

if ! [[ -d /var/log/pseudotest ]]; then
    mkdir /var/log/pseudotest
fi
touch /var/log/pseudotest/${DATE}.log

gunicorn --pid gunicorn.pid --workers=2 --access-logfile /var/log/pseudotest/${DATE}.log -D test_django.wsgi -b 0.0.0.0:80