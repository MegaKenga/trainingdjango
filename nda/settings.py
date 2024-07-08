"""
Django settings for nda project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv


load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'debug_toolbar',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'catalog.apps.CatalogConfig',
    'files.apps.FilesConfig',
    'cart.apps.CartConfig',
    'nda_email.apps.NdaEmailConfig',
    'django_cleanup',
    'django_sendfile',
    'django_celery_results',
    'core.apps.CoreConfig',
    'sorl.thumbnail',
    'tinymce'
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
]


INTERNAL_IPS = [
    '127.0.0.1',
]

ROOT_URLCONF = 'nda.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'core/templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'cart.context_processors.cart',
            ],
        },
    },
]

# helping pycharm to find templates
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

WSGI_APPLICATION = 'nda.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'another_db'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_USER_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

CACHES = {
    "default": {
        # "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "BACKEND": 'django.core.cache.backends.dummy.DummyCache',
        "LOCATION": "redis://127.0.0.1:6379",
    }
}

# CELERY SETTINGS
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = os.getenv('TIMEZONE')
CELERY_RESULT_BACKEND = 'django-db'
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True

# CELERY FILES UPLOAD SETTINGS
TEMPORARY_UPLOAD_ROOT = 'tmp/'
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = os.getenv('TIMEZONE')

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    (os.path.join(BASE_DIR, "core/static")),
    BASE_DIR / "static"
]
STATIC_ROOT = os.path.join(BASE_DIR, "/static/")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'


# DJANGO_SENDFILE SETTINGS
PRIVATE_ROOT = os.getenv('PRIVATE_PATH')
SENDFILE_ROOT = 'private/'
SENDFILE_BACKEND = 'django_sendfile.backends.simple'


SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


# EMAIL_SENDER SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.getenv('HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('HOST_PASSWORD')
RECIPIENT_EMAIL = os.getenv('RECIPIENT')
EMAIL_PORT = os.getenv('PORT', '587')
EMAIL_USE_TLS = True


# YANDEX CAPTCHA SETTINGS
SECURE_REFERRER_POLICY = 'no-referrer-when-downgrade'
YACAPTCHA_SERVER = os.getenv('SERVER_KEY')


# TINYMCE SETTINGS
TINYMCE_JS_URL = os.path.join(BASE_DIR, MEDIA_URL, "tinymce/js/tinymce/tinymce.min.js")
TINYMCE_COMPRESSOR = False
TINYMCE_SPELLCHECKER = True
TINYMCE_DEFAULT_CONFIG = {
    "height": "320px",
    "width": "960px",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
    "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
    "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
    "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
    "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
    "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
    "language": "ru_RU"
}
