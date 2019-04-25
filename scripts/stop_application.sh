#!/usr/bin/env bash

cd /home/ubuntu/pseudotest/test_django

kill $(cat gunicorn.pid) |: