# weather
simple weather web app that shows actual weather conditions according to chosen city

## requirements
- python
- django
- psycopg2
- requests

## install
- install and run postgres database server for your system
- make a new db called 'weather' in it
- set up your venv
- ```pip install -r requirements.txt```

## first init
- migrate database ```python manage.py makemigrations``` and ```python manage.py migrate```
- create superuser ```python manage.py createsuperuser``` with name and pwd
- run server ```python manage.py runserver```
- then navigate to ```http://127.0.0.1:8000/admin``` and create your own db entries (cities)

## run
- go to ```http://127.0.0.1:8000```

## notes
- i just wanted to try using API requests