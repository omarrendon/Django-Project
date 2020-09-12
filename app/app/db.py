import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

POSTGRES = {
  'default' : {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME' : 'Omar',
    'USER' : 'agavesoft',
    'PASSWORD' : 'becarios2020',
    'HOST' : '3.237.20.227',
    'PORT' : '5432'
  }
}