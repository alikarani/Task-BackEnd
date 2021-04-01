heroku config:set DISABLE_COLLECTSTATIC=1

release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn pythonchalange.wsgi