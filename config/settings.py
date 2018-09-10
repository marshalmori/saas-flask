DEBUG = True

# SERVER_NAME = 'localhost:8000'
SERVER_NAME = 'local.docker:8000'
SECRET_KEY = 'insecurekeyfordev'

# Flask-Mail
MAIL_DEFAULT_SENDER = 'marshalmori@gmail.com'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'marshalmori@gmail.com'
MAIL_PASSWORD =  'passwordhere'

# Celery
CELERY_BROKER_URL = 'redis://devpassword@redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://devpassword@redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5
