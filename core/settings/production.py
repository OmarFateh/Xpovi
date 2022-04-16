from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'amazon_clone',
#         'USER': 'rootuser',
#         'HOST': 'localhost',
#         'PASSWORD': os.environ.get('DB_PASSWORD'),
#         'PORT': '3306',
#     }
# }