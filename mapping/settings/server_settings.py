from .base import *
DEBUG = False
ALLOWED_HOSTS = ["gis.feyton.co.rw", '127.0.0.1', 'https://gis.feyton.co.rw']

STATIC_ROOT = '/home/igityopp/gis.feyton.co.rw/static'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/igityopp/git.feyton.co.rw/media'
