from base import *
import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = open(os.path.join(
                os.path.dirname(__file__), '..', '..', 'conf', 'session_key')).read()

# Compress static files offline
# http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE

COMPRESS_OFFLINE = True

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

ALLOWED_HOSTS = [get_env_variable("HOST_NAME"), ]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME":  '{{ wagtail_db_name}}',
        "USER": '{{ wagtail_db_user }}',
        "PASSWORD": '{{ wagtail_db_pass }}',
        "HOST": '{{ wagtail_db_host }}',
    }
}

INSTALLED_APPS += (
    "wagtail.contrib.wagtailfrontendcache",
    'gunicorn',
)

# support opbeat
# MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#
#     'wagtail.wagtailcore.middleware.SiteMiddleware',
#     'wagtail.wagtailredirects.middleware.RedirectMiddleware',
# )

WAGTAIL_SITE_NAME = 'supergravity_main'

# Send notification emails as a background task using Celery,
# to prevent this from blocking web server threads
# (requires the django-celery package):
# http://celery.readthedocs.org/en/latest/configuration.html

# import djcelery
#
# djcelery.setup_loader()
#
# CELERY_SEND_TASK_ERROR_EMAILS = True
# BROKER_URL = 'redis://'


# Use Redis as the cache backend for extra performance
# (requires the django-redis-cache package):
# http://wagtail.readthedocs.org/en/latest/howto/performance.html#cache

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '{{redis_host}}:{{redis_port}}',
        'KEY_PREFIX': 'supergravity_main',
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
            'TIMEOUT': 300
        }
    }
}

DEFAULT_FROM_EMAIL =  get_env_variable('EMAIL_FROM')
EMAIL_USE_TLS = True
EMAIL_HOST = get_env_variable('EMAIL_HOST')
EMAIL_HOST_USER = get_env_variable('EMAIL_USER')
EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_PASSWD')
EMAIL_PORT = 587

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers':     ['mail_admins'],
            'level':        'ERROR',
            'propagate':    False,
        },
        'django.security': {
            'handlers':     ['mail_admins'],
            'level':        'ERROR',
            'propagate':    False,
        },
    },
}
