import os
import dj_database_url
from .settings import *

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'))
    }

DEBUG = False
TEMPLATE_DEBUG = False
# ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS'), 'localhost']
ALLOWED_HOSTS = ['python230-ubuntu8000005.westus.cloudapp.azure.com', 'localhost']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
SECRET_KEY = 'adkDf9brpZSvyY6F5sxqE7F579pPGL72y98AaDCaBQ9dHZ9XBT'
# SECRET_KEY = os.environ.get('SECRET_KEY', 0)
DATABASE_URL = 'postgres://postgres:8dB8t!c7bFHFnThYw@python-2303818414376005.westus.cloudapp.azure.com:5432/djangoblog'
