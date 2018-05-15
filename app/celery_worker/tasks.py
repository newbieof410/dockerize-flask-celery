import time

from app.celery_worker import celery


@celery.task
def long_time_task():
    print('task begins')
    time.sleep(10)
    print('task finished')
