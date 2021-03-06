"""
Django settings for Blog project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g626!i8sca^_5bkc)!5y-d$s-acx*^bg%vm8fttjt6twcq9g03'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'ItBoom',
    'tinymce',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


TINYMCE_DEFAULT_CONFIG = {
'height': 360,
'width': 1120,
'cleanup_on_startup': True,
'custom_undo_redo_levels': 20,
'selector': 'textarea',
'theme': 'modern',
'plugins': '''
    textcolor save link image media preview codesample contextmenu
    table code lists fullscreen insertdatetime nonbreaking
    contextmenu directionality searchreplace wordcount visualblocks
    visualchars code fullscreen autolink lists charmap print hr
    anchor pagebreak
    ''',
'toolbar1': '''
    fullscreen preview bold italic underline | fontselect,
    fontsizeselect | forecolor backcolor | alignleft alignright |
    aligncenter alignjustify | indent outdent | bullist numlist table |
    | link image media | codesample |
    ''',
'toolbar2': '''
    visualblocks visualchars |
    charmap hr pagebreak nonbreaking anchor | code |
    ''',
'contextmenu': 'formats | link image',
'menubar': True,
'statusbar': True,
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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
TINYMCE_COMPRESSOR = False

TINYMCE_FILEBROWSER = True

TINYMCE_SPELLCHECKER = True

FILEBROWSER_DIRECTORY = ''

DIRECTORY = ''

FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.pdf', '.tiff'],
    'Document': ['.doc', '.docx', '.rtf', '.txt', '.xls', '.xslx', '.csv', '.ppt', '.pptx'],
    'Video': ['.mov', '.wmv', '.mpeg', '.mpg', '.avi', '.rm'],
    'Audio': ['.mp3', '.mp4', '.wav', '.aiff', '.midi', '.m4p'],
}


STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_cdn')

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media_cdn')

STATICFILES_DIRS = [
    os.path.join(os.path.dirname(BASE_DIR), 'resource')
]

SITE_ID = 1
