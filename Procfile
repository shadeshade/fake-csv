web: gunicorn config.wsgi
worker: celery -A config.celery:app worker -l info