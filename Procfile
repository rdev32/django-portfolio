web: python manage.py loaddata db.json
web: python manage.py makemigrations control
web: python manage.py migrate
web: gunicorn -b 0.0.0.0:$PORT portfolio.wsgi