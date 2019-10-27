import os
import dj_database_url
from .settings import *

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'))
    }

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS'), 'localhost']
print(ALLOWED_HOSTS)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
print(os.getenv('SECRET_KEY', 0))
SECRET_KEY = os.environ.get('SECRET_KEY', 0)
