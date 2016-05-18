from .base import *
import os

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY', 'turkey')
print ('SECRET_KEY', SECRET_KEY)
