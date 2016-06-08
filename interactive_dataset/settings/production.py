import os
from .base import *

import dj_database_url  # For heroku database connection

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY', None)# 'ze-local-run123')

## Database settings via Heroku url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

## Email settings in Herok Config Vars

EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = os.environ['EMAIL_PORT']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
DEFAULT_FROM_EMAIL = os.environ['DEFAULT_FROM_EMAIL']
EMAIL_USE_TLS = os.environ['EMAIL_USE_TLS']
