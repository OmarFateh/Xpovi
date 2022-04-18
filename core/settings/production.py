from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd6lavct8j3msf6',
        'USER': 'urrrwzwcdtzpqg',
        'HOST': 'ec2-34-247-72-29.eu-west-1.compute.amazonaws.com',
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'PORT': '5432',
    }
}
