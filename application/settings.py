"""
Django settings for application project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys
import pymysql
from dotenv import load_dotenv
from django.template import RequestContext
from application.constants import ROOT_NAME
from application.submodules import logger
from django.urls import reverse

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_ROOT_PATH = os.path.join(BASE_DIR, 'application')
sys.path.append(APP_ROOT_PATH)

load_dotenv(os.path.join(BASE_DIR, '.env'))
pymysql.install_as_MySQLdb()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.getenv('DEBUG', '1')))

ALLOWED_HOSTS = ['*']

# Application definition

# 認証時に利用するユーザーモデル
AUTH_USER_MODEL = 'auth.User'

AUTO_LOAD_DOMAINS = [
    'application',
    'resources',
    'index',
    'accounts',
    'books',
    'categories',
    'reviews',
    'memos',
    'orderhistories',
]

# メモ： moduleがapp名になる
# 例：'modules.book' => modulesはパッケージ名でbookがmoduleなのでapp名
AUTO_LOAD_MODULES = [
    'modules.book',
    'modules.orderbook',
    'modules.review',
    'modules.memo',
    'modules.profile',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrapform',
]

for domain in AUTO_LOAD_DOMAINS:
    INSTALLED_APPS.append(domain)

for domain in AUTO_LOAD_MODULES:
    INSTALLED_APPS.append(domain)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

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
                'resources.templates.context_processors.constants',
            ],
        },
    },
]

for domain in AUTO_LOAD_DOMAINS:
    TEMPLATES[0]['DIRS'] = os.path.join(
        BASE_DIR, domain.replace('.', '/') + '/templates')

WSGI_APPLICATION = 'wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE_NAME', 'empty_db_name'),
        'USER': os.getenv('DATABASE_USER', 'empty_db_user'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'empty_db_password'),
        'HOST': os.getenv('DATABASE_HOST', 'empty_db_host'),
        'PORT': os.getenv('DATABASE_PORT', 'empty_db_port'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

# 長すぎてpep8違反になるので切り分け
_pv_package_name = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': _pv_package_name + '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': _pv_package_name + '.MinimumLengthValidator',
    },
    {
        'NAME': _pv_package_name + '.CommonPasswordValidator',
    },
    {
        'NAME': _pv_package_name + '.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(APP_ROOT_PATH, 'static'),
)


def get_debug_or_prod() -> str:
    return 'DEBUG' if DEBUG else 'PRODUCTION'


# 置き換えるlogbookに置き換える予定
LOGGING = {
    'version': 1,
    'formatters': {  # 出力フォーマットを文字列形式で指定する
        'all': {  # 出力フォーマットに`all`という名前をつける
            'format': '\t'.join([
                '[%(levelname)s]',
                'asctime:%(asctime)s',
                'module:%(module)s',
                'message:%(message)s',
                'process:%(process)d',
                'thread:%(thread)d',
            ])
        },
    },
    'handlers': {
        'file': {
            'level': get_debug_or_prod(),  # DEBUG以上のログを取り扱うという意味
            'class': 'logging.FileHandler',  # ログを出力するためのクラスを指定
            'filename': os.path.join(BASE_DIR, 'django.log'),  # どこに出すか
            'formatter': 'all',
        },
        'console': {
            'level': get_debug_or_prod(),
            # こちらは標準出力に出してくれるクラスを指定
            'class': 'logging.StreamHandler',
            'formatter': 'all'
        },
    },
    'loggers': {  # どんなloggerがあるかを設定する
        'webook_logger': {  # loggerを定義
            'handlers': ['file', 'console'],
            'level': get_debug_or_prod(),
        },
    },
}

# 画像用
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = '/books'
LOGIN_URL = '/accounts/login'
LOGOUT_REDIRECT_URL = LOGIN_URL
