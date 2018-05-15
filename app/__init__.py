import os

from celery import Celery
from flask import Flask

from config import config


def create_app(config_name, register_blueprint=True):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    if register_blueprint:
        from app.test_celery import test_celery as test_celery_blueprint
        app.register_blueprint(test_celery_blueprint)

    return app


def make_celery_app(app=None):
    app = app or create_app(os.getenv('FLASK_CONFIG') or 'default',
                            register_blueprint=False)

    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )

    celery.conf.update(app.config)

    class ContextTask(celery.Task):

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
