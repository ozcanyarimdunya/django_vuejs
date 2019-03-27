#!/usr/bin/env bash

#set -o errexit
#set -o pipefail
#set -o nounset

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn config.wsgi -b 0.0.0.0:8000 -w 4 --chdir=/app --reload