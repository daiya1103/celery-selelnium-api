#!/bin/bash

echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
gunicorn config.wsgi:application --bind 127.0.0.1:8000

exec "$@"