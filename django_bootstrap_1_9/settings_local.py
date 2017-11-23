import os
from ConfigParser import SafeConfigParser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = SafeConfigParser()
config.read(BASE_DIR + '/.env')

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME':'ecom_again',
        'USER': 'lakshay',
        'PASSWORD': 'lakshay',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
else:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
