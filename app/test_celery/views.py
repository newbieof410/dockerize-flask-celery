from flask import jsonify

from app.celery_worker import tasks
from app.test_celery import test_celery


@test_celery.route('/', methods=['GET'])
def index():
    result = tasks.long_time_task.delay()
    return jsonify(msg='request received', result_id=result.id)
