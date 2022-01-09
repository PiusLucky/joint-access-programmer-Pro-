build: heroku config:set DISABLE_COLLECTSTATIC=1
release: python manage.py migrate
web: gunicorn jap.wsgi --log-file -
