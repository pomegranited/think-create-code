"""
Django settings for gallery app.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm=2w&k4)f^1-ii04p(b88%_&%$w!(s)p)%gqvh@ac498566p+s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

# ADELAIDEX_LTI.*_URLs and OAUTH_CREDENTIALS are initialised below, per environment
ADELAIDEX_LTI = {
    'LOGIN_URL': None,
    'COURSE_URL': '',
    'ENROL_URL': '',
    'LINK_TEXT': 'Code101x Think.Create.Code',
    'PERSIST_NAME': 'lti-gallery',
    'PERSIST_PARAMS': ['next'],
    'STAFF_MEMBER_GROUP': 1,
}

# Disqus integration
ADELAIDEX_LTI_DISQUS = {
    'SHORTNAME': 'thinkcreatecodegallery',
    'DEFAULT_EMAIL': '{user.username}@edx.org',
    'IDENTIFIER': 'a/%d',
    'SECRET_KEY': 'CH2OwPJpIwukfaiE2EbBAwALZxYsHcgii3TzpqrmFbQ9cgfiaHGfXXb48k8uMItq',
    'PUBLIC_KEY': 'jbXXUtp4uRwQwU0DAbHQnaG6X6JIk83ZHyQksEbQJ4y0AeJSFvzOY43PkSV2fPkh',
}

# Default logging config
LOGGING_CONFIG_FILE = os.path.join(BASE_DIR, 'gallery', 'logging-prd.conf')

# Determine enviroment we're running in
ENVIRONMENT = os.environ.get("DJANGO_GALLERY_ENVIRONMENT", "production-3T2015")

if ENVIRONMENT == 'production-2T2015':

    DATABASES = {
        'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'processingjs_gallery',
             'USER': 'gallery_rw',
             'PASSWORD': 'gAll3rY-rw',
        }
    }
    STATIC_URL = '/think.create.code/static/'
    ALLOWED_HOSTS = ['*']

    # Link to a live course are contains a Code Gallery LTI unit
    ADELAIDEX_LTI['COURSE_URL'] = 'https://courses.edx.org/courses/course-v1:AdelaideX+Code101x+2T2015/courseware/0655ee1be221492b90c043cc1d6cb648/87818d7c405143b7b642c6bbbe793bc7/'
    ADELAIDEX_LTI['ENROL_URL'] = 'https://www.edx.org/course/think-create-code-adelaidex-code101x'
    ADELAIDEX_LTI['LOGIN_URL'] = ADELAIDEX_LTI['COURSE_URL']
    LTI_OAUTH_CREDENTIALS = {
        'code101x_2t2015': 'D8RoantdHgp0aABAGNNv',
    }

    # https://lti-adx.adelaide.edu.au/think.create.code/gallery/share
    SHARE_URL = 'https://bit.ly/1A3Kdoy'

    # http://loco.services.adelaide.edu.au/think.create.code/gallery/share
    #SHARE_URL = 'https://bit.ly/1MaoZG4'

    ALLOW_ANALYTICS = True

    ADELAIDEX_LTI_DISQUS['IDENTIFIER'] = '2t2015/a/%d'

elif ENVIRONMENT == 'production-3T2015':

    DEBUG=True # XXX

    DATABASES = {
        'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'processingjs_gallery_3t2015',
             'USER': 'gallery_rw',
             'PASSWORD': 'gAll3rY-rw',
        }
    }
    STATIC_URL = '/think.create.code/3t2015/static/'
    ALLOWED_HOSTS = ['*']

    # FIXME Link to a live course are contains a Code Gallery LTI unit
    ADELAIDEX_LTI['COURSE_URL'] = 'https://courses.edx.org/courses/course-v1:AdelaideX+Code101x+2T2015/courseware/0655ee1be221492b90c043cc1d6cb648/87818d7c405143b7b642c6bbbe793bc7/'
    ADELAIDEX_LTI['ENROL_URL'] = 'https://www.edx.org/course/think-create-code-adelaidex-code101x'
    ADELAIDEX_LTI['LOGIN_URL'] = ADELAIDEX_LTI['COURSE_URL']
    LTI_OAUTH_CREDENTIALS = {
        'code101x_3t2015': 'ja2k9wQwAX31nfjgQafB',
    }

    # https://lti-adx.adelaide.edu.au/think.create.code/3t2015/gallery/share
    SHARE_URL = 'https://bit.ly/1JjomIB'

    ALLOW_ANALYTICS = True

    ADELAIDEX_LTI_DISQUS['IDENTIFIER'] = '3t2015/a/%d'

elif ENVIRONMENT == 'development':

    # Runs via ./manage.py runserver
    DEBUG = True
    TEMPLATE_DEBUG = True
    DATABASES = {
        'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'processingjs_gallery_dev',
             'USER': 'gallery_rw',
             'PASSWORD': 'gAll3rY-rw',
        }
    }
    STATIC_URL = '/static/'
    ALLOWED_HOSTS = []

    # http://loco.services.adelaide.edu.au:8000/share
    SHARE_URL = 'https://bit.ly/1A3JLXA'

    ALLOW_ANALYTICS = False

    ADELAIDEX_LTI_DISQUS['IDENTIFIER'] = 'dev/a/%d'

    LOGGING_CONFIG_FILE = os.path.join(BASE_DIR, 'gallery', 'logging-dev.conf')

elif ENVIRONMENT == 'testing':

    # Runs via ./manage.py test
    DEBUG = False
    TEMPLATE_DEBUG = False
    DATABASES = {
        'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': os.path.join(BASE_DIR, 'test_db.sqlite3'),
        }
    }
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    ALLOWED_HOSTS = ['localhost']

    # http://0.0.0.0:8080/share
    SHARE_URL = 'https://bit.ly/1zMTDl8'

    ALLOW_ANALYTICS = False

# else - error: no database defined


# Configure logging
from logging import config as logging_config
logging_config.fileConfig(LOGGING_CONFIG_FILE)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rulez',
    'database_files',
    'django_adelaidex.util',
    'django_adelaidex.lti',
    'artwork',
    'exhibitions',
    'submissions',
    'votes',
)

MIDDLEWARE_CLASSES = (
    'django_adelaidex.util.middleware.WsgiLogErrors',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_auth_lti.middleware.LTIAuthMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'csp.middleware.CSPMiddleware',
    'django_adelaidex.util.middleware.P3PMiddleware',
    'django_adelaidex.lti.middleware.TimezoneMiddleware',
)

ROOT_URLCONF = 'gallery.urls'

WSGI_APPLICATION = 'gallery.wsgi.application'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEFAULT_FILE_STORAGE = 'database_files.storage.DatabaseStorage'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join( BASE_DIR, 'static' ),
)


VIRTUALLIB_BASE_DIR = os.path.join( BASE_DIR, '..', '.virtualenv', 'lib', 'python2.7', 'site-packages' )

TEMPLATE_DIRS = (
    os.path.join( BASE_DIR, 'templates' ),
    # TODO Hopefully fixed in Django 1.8
    os.path.join( VIRTUALLIB_BASE_DIR, 'django_adelaidex', 'util', 'templates' ),
    os.path.join( VIRTUALLIB_BASE_DIR, 'django_adelaidex', 'lti', 'templates' ),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'django_adelaidex.util.context_processors.analytics',
    'django_adelaidex.util.context_processors.referer',
    'django_adelaidex.util.context_processors.base_url',
    'django_adelaidex.lti.context_processors.lti_settings',
    'django_adelaidex.lti.context_processors.disqus_settings',
    'django_adelaidex.lti.context_processors.disqus_sso',
)

# P3P header
P3P_HEADER_KEY = 'P3P:CP'
P3P_HEADER_VALUE = 'IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT'

# Content Security Policy
CSP_DEFAULT_SRC = (
    "'self'",
)
CSP_SCRIPT_SRC = (
    "'self'",
    "'unsafe-inline'", # artwork/_render.html, artwork/edit.html
    "https://www.google-analytics.com",
    "a.disquscdn.com",
    "thinkcreatecodegallery.disqus.com",
)
CSP_IMG_SRC = (
    "'self'",
    "data:",
    "https://www.google-analytics.com",
    "referrer.disqus.com", 
    "a.disquscdn.com",
)
CSP_STYLE_SRC = (
    "'self'",
    "'unsafe-inline'", # modernizr.js
    "a.disquscdn.com",
)
CSP_FRAME_SRC = (
    "'self'", 
    "disqus.com",
)


# Authentication
LOGIN_URL = 'login'

from django.core.urlresolvers import reverse_lazy
LOGIN_REDIRECT_URL = reverse_lazy('home')

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', # Django's default auth backend
    'django_auth_lti.backends.LTIAuthBackend',
    'rulez.backends.ObjectPermissionBackend',
]

AUTH_USER_MODEL = 'lti.User'
