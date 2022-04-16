from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd8qdqg1rk7i8cj',
        'USER': 'iuydmznetafnho',
        'HOST': 'ec2-52-18-116-67.eu-west-1.compute.amazonaws.com',
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'PORT': '5432',
    }
}

