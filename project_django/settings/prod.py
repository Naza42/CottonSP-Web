from .base import *

DEBUG = False 

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': BASE_DIR / 'db.sqlite3',
        'PASSWORD' : 'ROOT',
        'PORT' : 3366,
        'HOST' : ''
    }
}