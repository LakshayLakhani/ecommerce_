import os
from ConfigParser import SafeConfigParser

DEBUG = False
config = SafeConfigParser()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config.read(BASE_DIR + '/.env')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config.get('staging', 'DBNAME'),
        'USER': config.get('staging', 'DBUSER'),
        'PASSWORD': config.get('staging', 'DBPASSWORD'),
        'HOST': config.get('staging', 'DBHOST'),
        'PORT': config.get('staging', 'DBPORT'),
    }
}

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
else:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': "{}/logs/django_access.log".format(BASE_DIR), # TODO: Add File Name
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'request_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': "{}/logs/django_access.log".format(BASE_DIR), # TODO: Add File Name
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}
