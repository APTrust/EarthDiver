"""
Django settings for dpnode project.

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
SECRET_KEY = 'ic8lmsbq5+m80e4g7$+ie&)(g)qz9wk^ws#53#217)z6g5m^2('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# IMPORTANT SET ONLY TO TRUE IN DEVELOPMENT ENVIRONMENT
DEV = False

ALLOWED_HOSTS = []

AUTH_PROFILE_MODULE = 'dpn.data.UserProfile'

# Default Settings.  Make real changes in localsettings
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'PAGINATE_BY': 20,
    'PAGINATE_BY_PARAM': 'page_size',
    'MAX_PAGINATE_BY': 500,
}

# Application definition

INSTALLED_APPS = (
    'grappelli', # Order required by module
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Dependency Modules
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    # Core DPN modules
    'dpn.data',
    'dpn.api',
    'dpn.client',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dpnode.urls'

WSGI_APPLICATION = 'dpnode.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# Support configurable localsettings.
# To setup just copy localsettings_dist.py to localsettings.py and
# set values as appropriate.
try:
    from dpnode.localsettings import *
except ImportError:
    import sys

    print('''Missing localsettings!  Please configure a version of
    localsettings.py for this app.  See localsettings_dist.py for details''')
    del sys