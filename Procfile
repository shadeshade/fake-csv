web: gunicorn config.wsgi
worker: celery -A config.celery worker -B --loglevel=info