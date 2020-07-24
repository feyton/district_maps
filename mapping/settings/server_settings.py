from .base import *
from decouple import config
DEBUG = True
ALLOWED_HOSTS = ["gis.feyton.co.rw", '127.0.0.1', 'https://gis.feyton.co.rw', "localhost"]

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
