from app import make_celery_app

celery = make_celery_app()

from app.celery_worker import tasks
