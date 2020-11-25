from .base import *
DEBUG = True
ALLOWED_HOSTS = []

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST_USER = 'no-reply@feyton.co.rw'


DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
