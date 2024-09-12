#!/bin/sh


echo Hello!!!!!!!
python3 manage.py collectstatic --noinput --clear
 
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

gunicorn -b '0.0.0.0:8000' django_app.wsgi:application


