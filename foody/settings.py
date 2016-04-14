"""
Django settings for foody project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
pj = os.path.join
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a6m*hp!whbcqjr2$syacry5+ysy_x2ey4u7(235g183)ijh7vn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_tml',
    'foody'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_tml.middleware.TmlControllerMiddleware',
]

ROOT_URLCONF = 'foody.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'foody.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'foody.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

TML = {
    'environment': 'dev',
    'application': {
        'key': '6c377447a542718bfd9fe0f5d8f11fae2827377bc4295db76667469db67bd8ed',
        'path': 'https://staging-api.translationexchange.com',
        'cdn_path': 'http://trex-snapshots.s3-us-west-1.amazonaws.com'},
    'monkeypatch': True,
    # 'cache': {
    #     'enabled': True,
    #     'adapter': 'djcache',
    #     'backend': 'django.core.cache.backends.memcached.MemcachedCache',
    #     'namespace': 'foody'
    # },
    'cache': {
        'enabled': True,
        'adapter': 'memcached',
        'backend': 'pylibmc',
        'namespace': 'foody'
    },
    'locale': {'subdomain': True, 'query_param': 'locale'},
    # 'cache': {
    #     'enabled': True,
    #     'adapter': 'file',
    #     'version': '20160312152203',
    #     'path': pj(BASE_DIR, 'tml/cache.test')
    #    # 'path': pj(os.path.dirname(BASE_DIR), 'tests/fixtures/snapshot.tar.gz')
    # },
    'agent': {
        'enabled': True,
        'type':    'agent',
        'host': 'https://tools.translationexchange.com/agent/staging/agent.min.js',
        'cache':   86400,  # timeout every 24 hours
        'force_injection': False
    },
    #'data_preprocessors': ('tml.tools.list.preprocess_lists',),
    'env_generators': ('tml.tools.viewing_user.get_viewing_user',),
    'logger': {
        'path': pj(BASE_DIR, 'logs', 'tml.log')
    },
    'strict_mode': True   # reraise exception rather than silent 
}
