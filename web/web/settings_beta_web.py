from settings_beta import *

DEBUG = False
TEMPLATE_DEBUG = False
THUMBNAIL_DEBUG = False
STATIC_URL = 'http://web.newtonproject.beta.diynova.com/static/'
DOMAIN = 'web.newtonproject.beta.diynova.com'
BASE_URL = 'http://web.newtonproject.beta.diynova.com'
MEDIA_URL = 'http://web.newtonproject.beta.diynova.com/filestorage/'

LOGGING_API_REQUEST = True
USE_TESTNET = True
ROOT_URLCONF = 'web.urls_web'
SESSION_COOKIE_NAME = 'nwsid'
