import os
import dj_database_url
from dotenv import load_dotenv

load_dotenv()
db_settings = os.getenv('DB_SETTINGS')

DATABASES = {
    'default': dj_database_url.parse(db_settings)
    }

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG', default=False)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', default=['localhost'])

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'en-en'

TIME_ZONE = 'Europe/Prague'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
