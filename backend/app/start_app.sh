#!/bin/bash

while ! nc -z db 5432; do sleep 1; done;

if [ "$APP_ENV" = "dev" ] ; then 
    python manage.py runserver 0.0.0.0:8000 ; 
else 
    python -m gunicorn main.wsgi --bind=0.0.0.0:8000 ; 
fi