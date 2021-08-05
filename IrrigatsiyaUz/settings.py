import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _  #for multi-language


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h9m=u73h12lwce5(k7o&sk!kzzx+7-5--qks^27e1n5b8xeq!b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

 
# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'accounts.apps.AccountsConfig',
    'my_works.apps.MyWorksConfig',
    
    'crispy_forms',
    'rest_framework',
    # 'django_cleanup',   signals.py added for auto cleaning
    'django_filters',
    'rest_framework.authtoken',
    'corsheaders',
    'phonenumber_field',
    'drf_yasg',
    'whitenoise',

]

# MIDDLEWARE_CLASSES = (
# 'livesync.core.middleware.DjangoLiveSyncMiddleware',
# )


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.locale.LocaleMiddleware", #for multi language
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# CORS_ORIGIN_WHITELIST = (
#     'localhost':3000,
#     )
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'IrrigatsiyaUz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'accounts.context_processors.notifications',
            ],
        },
    },
]

WSGI_APPLICATION = 'IrrigatsiyaUz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':os.path.join(BASE_DIR, 'db.sqlite3')
        # 'NAME':'irrigatsiyauz',
        # 'HOST':'*',
        # 'PORT':5432,
        # 'USER':'postgres',
        # 'PASSWORD':'testing321',
    }
}


#DJANGO REST FRAMEWORK
REST_FRAMEWORK = {
 
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE':10, 
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/


MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
MODELTRANSLATION_FALLBACK_LANGUAGES = ('en', 'uz', )
MODELTRANSLATION_PREPOPULATE_LANGUAGES = ('en')

LANGUAGES = (
    ("uz", _('Uzbek')),
    ("ru", _('Russian')),
    ("en", _('English')),
)
LANGUAGE_CODE = 'uz'
TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

#  Contains the path list where Django should look into for django.po files for all supported languages
LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field


#EMAIL_CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'abrorjonaxmadov21@gmail.com'
EMAIL_HOST_PASSWORD = 'testing321'

LOGOUT_REDIRECT_URL = '/me/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
