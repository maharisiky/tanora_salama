#!/bin/bash
# Exécuter les migrations
python manage.py makemigrations
python manage.py migrate

# Collecter les fichiers statiques
python manage.py collectstatic --noinput

python manage.py seed_all

exec gunicorn bot.wsgi:application --workers 1 --bind 0.0.0.0:8000