from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "storefront",
        "HOST": "127.0.0.1",
        "USER": "root",
        "PASSWORD": "1234",
        'OPTIONS': {
           "init_command": "SET GLOBAL max_connections = 100000",
    }
    }
}