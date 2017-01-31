"""
Django settings for mediamapper project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [

]

#Application Definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'home',
    'medioschile',
    'medioscolombia', 
    'haystack',	
    'redactor',		
    'select2',
    'forms_builder.forms',
    'django_mandrill',
#    'simple_open_graph',
#    'rest_framework',
#    'exportdata',
#    'fixture_magic',
#    'mediosargentina',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.template.context_processors.tz',
    'django.core.context_processors.static',
    'django.template.context_processors.csrf',
    'django.contrib.messages.context_processors.messages',
    'django.template.context_processors.debug',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',	
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mmapper',
        'USER': '',
        'PASSWORD': '',
    }
}

ADMINS = ('','@')

# Search Haystack
import os
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.search_backends.FoldingWhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 1000
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor' 
# 
# 
#
# mandrill api
MANDRILL_API_KEY = ""

# Configuracion de mail
EMAIL_BACKEND='django_mandrill.mail.backends.mandrillbackend.EmailBackend'
EMAIL_HOST='smtp.mandrillapp.com'
EMAIL_PORT=587
EMAIL_HOST_USER=''
EMAIL_HOST_PASSWORD=''

ROOT_URLCONF = 'mediamapper.urls'

WSGI_APPLICATION = 'mediamapper.wsgi.application'

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.request',)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docODs.djangoproject.com/en/1.7/howto/static-fOCiles/ 

STATIC_ROOT = ''
STATIC_URL = ''
STATICFILES_DIRS = (
    "",
)


GRAPPELLI_ADMIN_TITLE = 'Mediamapper Admin'
ENV_PATH = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(ENV_PATH, 'media')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

REDACTOR_OPTIONS = {'lang': 'es', 'plugins': ['imagemanager','video']}
REDACTOR_UPLOAD = 'uploads/'

from settings_local import *
