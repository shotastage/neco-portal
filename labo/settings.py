"""
Django settings for labo project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from labo.db_secret import database_setting


try:
    RUNNING_MODE = os.environ["NSYS_RUNNING_MODE"]
except:
    RUNNING_MODE = "devel"

try:
    DEBUG_LOG_MODE = os.environ["DEBUG_LOG_MODE"]
except:
    DEBUG_LOG_MODE = "FALSE"



# NECO Portal Configurations
try:
    SEASONABLE_EMOJI = os.environ["SEASONABLE_EMOJI"] + "  "
except:
    SEASONABLE_EMOJI = ""

try:
    APPLICATION_NAME = os.environ["APP_NAME"]
except:
    APPLICATION_NAME = "NECO Portal"


try:
    SLACK_INCOMING_TOKEN = os.environ["SLACK_INCOMING_TOKEN"]

except:
    SLACK_INCOMING_TOKEN = ""





# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
try:
    SECRET_KEY = os.environ["SECRET_KEY"]
except:
    SECRET_KEY = '8m(#wph6wde_6io&ox!2tmf)b*7@0!^7fqg9q&l^^mktg^@q6p'


# SECURITY WARNING: don't run with debug turned on in production!
if RUNNING_MODE == "production":
    DEBUG = False
else:
    DEBUG = True

if DEBUG_LOG_MODE == "TRUE":
    DEBUG = True


if RUNNING_MODE == "production":
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = ["*"]



if RUNNING_MODE == "devel":
    print("************************************************************************************")
    print("MODE: ", RUNNING_MODE)
    print("BASE Directory: ", BASE_DIR)
    print("Static Directory: ", os.path.join(BASE_DIR, 'frontend', 'dist', 'static'))
    print("************************************************************************************")

# Application definition

INSTALLED_APPS = [
    'register.apps.RegisterConfig',
    'setup.apps.SetupConfig',
    'app.apps.AppConfig',
    'enrollment.apps.EnrollmentConfig',
    'bgport.apps.BgportConfig',
    'news.apps.NewsConfig',
    'manager.apps.ManagerConfig',
    'home.apps.HomeConfig',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'whitenoise.runserver_nostatic',  # < Per Whitenoise, to disable built in
    'rest_framework',
    #'webpack_loader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'labo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join('frontend', 'dist'), 'views'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
                'labo.context_processors.site_common_text'
            ],
        },
    },
]

WSGI_APPLICATION = 'labo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

if RUNNING_MODE == "production":
    DATABASES = database_setting
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_URL = 'register:login'
LOGIN_REDIRECT_URL = 'register:top'


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ja-JP'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
MIDDLEWARE_CLASSES = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

STATIC_URL = '/static/'


if RUNNING_MODE == "devel":
    #STATIC_ROOT = os.path.join('frontend', 'dist', 'static')
    STATICFILES_DIRS = (os.path.join('frontend', 'dist', 'static'),
    os.path.join('frontend', 'generates'),
    )
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_DIRS = (os.path.join('frontend', 'dist', 'static'),
    os.path.join('frontend', 'generates'),
    )
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
