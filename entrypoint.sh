#!/bin/bash

python manage.py makemigrations
python manage.py migrate

echo "hello-----------------------"

exec gunicorn --bind 0.0.0.0:8000 myfirstblog.wsgi
