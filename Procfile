web: gunicorn config.wsgi
worker: celery -A config worker -l info -B
