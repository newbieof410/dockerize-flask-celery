class Config:
    CELERY_RESULT_BACKEND = 'rpc://'
    CELERY_BROKER_URL = 'pyamqp://admin:admin-pass@rabbit:5672//'


config = {
    'default': Config
}
