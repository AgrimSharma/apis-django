"""
Django settings for doctorlog project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9gzoa3j(*%3lkl00^#tb3i@pex*#hk=0k(2b9fq8_ez_bl)9-)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False
ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]


# Application definition

INSTALLED_APPS = [
    'suit',
    "corsheaders",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'modules',
    'symptomsrecord',
    "vitalsrecord",
    'doctor'
]

MIDDLEWARE_CLASSES = [
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True 
ROOT_URLCONF = 'doctorlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'doctorlog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db1.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
      ],
    'HIDE_DOCS': True,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}
SUIT_CONFIG = {
    'LIST_PER_PAGE': 20,
    'MENU': (
        'sites',

        {'label': 'User', 'icon': 'icon-user', 'models': ('modules.Users',),
         'permissions': 'auth.user'},
        "-",

        {'label': 'Symptoms', 'icon': 'None', 'permissions': 'auth.user',
         "name": "Symptoms", 'models': ('symptomsrecord.SymptomsDef',
                                        'symptomsrecord.SymptomsUser',
                                        'symptomsrecord.SymptomsRecord',)},
        '-',

        {'label': 'Vitals', 'icon': 'None', 'permissions': 'auth.user',
         'models': ('vitalsrecord.Vitals', 'vitalsrecord.VitalReport')},
        '-',
        {'label': 'Doctor', 'icon': 'None', 'permissions': 'auth.user',
         'models': ('doctor.Doctor', 'doctor.DoctorPatient',
                    'doctor.DoctorAppointment',)},
        )
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
