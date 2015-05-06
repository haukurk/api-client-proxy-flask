import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

ADMINS = frozenset(['haukur@hauxi.is'])
SECRET_KEY = 'S0m3AwesomeKey'

SQLALCHEMY_DATABASE_URI = 'sqlite://database/' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

API_PROXY_URL = "https://itapi.samskip.com/"
API_KEY = "SomeAPIKEY!RWEFASDFASDFCAFR#$GSD"
API_VERSION = "v1.1"

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = "S0m3AwesomeKey."

STATIC_FOLDER_DEV = 'D:\' # needs to be specified for windows.

# Sentry URL
SENTRY_DSN = 'http://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@sentry.corp.is/2'