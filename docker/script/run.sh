#!/usr/bin/env bash

#python manage.py collectstatic --noinput
#python manage.py makemigrations
#python manage.py migrate
#exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 4 --reload
#
#
set -o errexit
set -o pipefail
set -o nounset

python manage.py makemigrations && \
python manage.py migrate && \
python manage.py collectstatic --noinput --verbosity 0 && \
gunicorn config.wsgi -b 0.0.0.0:8000 -w 4 --chdir=/app --reload