import os
from .settings_base import BASE_DIR, INSTALLED_APPS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}


if os.environ.get('DJANGO_DEBUG') == 'True':
    # Hakan's Settings:
    INSTALLED_APPS += [
        'django_extensions',
    ]
