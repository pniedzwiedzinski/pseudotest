#!/usr/bin/env bash

set -x
set -ueo pipefail

cd /home/ubuntu/pseudotest/test_django

cp django.nginxconf /etc/nginx/sites-available
ln -s /etc/nginx/sites-available/django.nginxconf /etc/nginx/sites-enabled/django.nginxconf

DATE=$(date +%H-%M-%S-%d-%m-%Y)

if ! [[ -d /var/log/pseudotest ]]; then
    mkdir /var/log/pseudotest
fi
touch /var/log/pseudotest/${DATE}.log

python3 manage.py collectstatic
gunicorn --pid gunicorn.pid --workers=2 --access-logfile /var/log/pseudotest/${DATE}.log -D test_django.wsgi --bind=unix:gunicorn.sock

service nginx restart