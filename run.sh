#!/usr/bin/env bash

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 4 --reload