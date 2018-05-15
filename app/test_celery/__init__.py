from flask import Blueprint

test_celery = Blueprint('test_celery', __name__)

from app.test_celery import views
