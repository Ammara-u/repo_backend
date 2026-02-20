import os
import dj_database_url
from .settings import *

from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = list(default_headers) + [
    'x-requested-with',
]

# Ensure these are also set
CORS_ALLOW_ALL_ORIGINS = True  
CORS_ALLOW_CREDENTIALS = True
ALLOWED_HOSTS = [os.environ.get('RENDER_EXTERNAL_HOSTNAME'), 'repo-backend-nlzr.onrender.com', 'localhost', '127.0.0.1']
# ALLOWED_HOSTS = [os.environ.get('RENDER_EXTERNAL_HOSTNAME')]
# Fixed the 'G' to 'F' and added the missing 'get'
# CSRF_TRUSTED_ORIGINS = ['https://' + os.environ.get('RENDER_EXTERNAL_HOSTNAME')] 

DEBUG = False
# Fixed '.gte' to '.get'
SECRET_KEY = os.environ.get('SECRET_KEY') 

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Ensure whitenoise is in requirements.txt
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ... rest of your code ...
# CORS_ALLOW_ALL_ORIGINS = True # Allow your React dev server to talk to Django
# CORS_ALLOWED_ORIGINS=['http://localhost:8081']

STORAGES={
    "default":{
        "BACKEND":"django.core.files.storage.FileSystemStorage",
    },
    "staticfiles":{
        "BACKEND":"whitenoise.storage.CompressedStaticFilesStorage"
    },
}

# In core/deployment_settings.py

# Delete the dj_database_url block and replace it with this:
DATABASES = {
    'default': {       
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ammara_InventoryApp',
        'HOST': '102.223.187.41',  # <--- REPLACE with your cPanel Shared IP
        'PORT': '3306',
        'USER': 'ammara_ammara',
        'PASSWORD': 'ammara@1104',
    }
}
# This block of code is configuring the database settings using the `dj_database_url` library in a
# Django project. Here's what it's doing:

# DATABASES={
#     'default':dj_database_url.config(
# default=os.environ['DATABASE_URL'],
# conn_max_age=600
#     )
# }

