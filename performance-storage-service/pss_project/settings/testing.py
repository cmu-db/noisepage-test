from .base import *

DEBUG = True
ALLOWED_HOSTS = ['incrudibles-testing.db.pdl.cmu.edu']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_environ_value('PSS_DATABASE_NAME'),
        'USER': get_environ_value('PSS_DATABASE_USER'),
        'PASSWORD': 'password',#get_environ_value('PSS_DATABASE_PASSWORD'),
        'HOST': 'timescaledb-service.performance',
        'PORT': int(get_environ_value('PSS_DATABASE_PORT', 5432)),
    }
}