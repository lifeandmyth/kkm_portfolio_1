"""
Django settings for kkm_portfolio project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

from . import myenv

import pymysql
pymysql.install_as_MySQLdb()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = myenv.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = myenv.DEBUG
DEBUG = myenv.DEBUG

# 기본, 인트라넷, aws 퍼블릭IPV4
ALLOWED_HOSTS = myenv.ALLOWED_HOSTS


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': myenv.NAME,
        'USER': myenv.USER,
        'PASSWORD' : myenv.PASSWORD,
        'HOST' : myenv.HOST,
        'PORT' : '3306',
        'OPTIONS':{
            'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'",
            # 'use_pure' : True
        }
    }
}
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #django_확장
    'django_extensions',
    #summernote Input 에디터
    'django_summernote',
    #all-auth lib 설정
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #google 인증 절차를 추가
    'allauth.socialaccount.providers.google',
    # cripsy-bootstrap4
    "crispy_forms",
    "crispy_bootstrap4",
    #django-markdownx
    'markdownx',
    #

    'diners',
    # diners, about_me(자기소개), portfolio 포함
    'single_pages',
    # 대시보드에 들어갈 식재료 목록&링크를 게시 // 대시보드
    'foodies_list', 
    #datas적용된 앱들
    'food_costs',

    # # cors 에러 처리
    # 'corsheaders',
]

MIDDLEWARE = [
    # # cors 에러 처리
   	# 'corsheaders.middleware.CorsMiddleware', #최상단에 추가해주기

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    
]

# CORS_ALLOWED_ORIGINS = [
# 	# 허용할 Origin 추가
#     "http://43.201.254.244/"
# ]


ROOT_URLCONF = 'kkm_portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'kkm_portfolio.wsgi:application'




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

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# if DEBUG==True:
#     # https://kante-kante.tistory.com/22
#     STATICFILES_DIRS = [os.path.join(BASE_DIR / 'static/')]
# # 

STATIC_ROOT = os.path.join(BASE_DIR, 'static_/')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



MEDIA_URL = '/_media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# all-auth lib 설정
AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    
]

SITE_ID = 1

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
LOGIN_REDIRECT_URL = '/diners/'

# django-crispy-forms 적용하기
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"