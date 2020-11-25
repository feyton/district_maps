from .base import *
from decouple import config
DEBUG = False
ALLOWED_HOSTS = ["gis.feyton.co.rw", '127.0.0.1', 'https://gis.feyton.co.rw', "localhost", '198.54.116.172', 'www.gis.feyton.co.rw', 'igiti.co.rw']

STATIC_ROOT = '/home/igityopp/gis.feyton.co.rw/static'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/igityopp/gis.feyton.co.rw/media'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'igityopp_gis',
        'USER': 'igityopp_gis_user',
        'PASSWORD': config("DB_PASS"),
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'STRICT_TRANS_TABLES',
        }
    }
}


SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
ADMINS = (('Feyton', 'info@feyton.co.rw'),)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = '198.54.116.172'
EMAIL_PORT = '465'
EMAIL_HOST_USER = 'no-reply@feyton.co.rw'
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", cast=str)
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
