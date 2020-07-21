from .base import *
DEBUG = True
ALLOWED_HOSTS = []

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
