# Django settings for ecomstore project.
import os
DEBUG = True
ENABLE_SSL = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('dotcom', 'dotcom900825@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ecomstore',                      # Or path to database file if using sqlite3.
        'USER': 'dotcom',                        # Not used with sqlite3.
        'PASSWORD': '4742488',                 # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/home/thomas/Downloads/ecomstore-master/templates/user_images'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	"/home/thomas/Downloads/ecomstore-master/templates",
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
  '/home/thomas/Downloads/ecomstore-master/templates',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'l06c=(^3f-$ku+@ez+l&amp;a3nc_@#cx=dh(mh6xmlg%h#aioka3j'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
  
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'ecomstore.SSLMiddleware.SSLRedirect',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ecomstore.urls'

LOGIN_REDIRECT_URL = '/accounts/my_account/'
# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ecomstore.wsgi.application'



INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'ecomstore.catalog',
    #'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    #'djangodblog',
    # Uncomment the next line to enable the admin:
     'django.contrib.admin',
     'ecomstore.utils',
     'ecomstore.cart',
     'ecomstore.accounts',
     'ecomstore.checkout',
     'ecomstore.search',
     
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

SITE_NAME = "Michael Collins Jewelry Store"
META_KEYWORDS = "Custom Jewelry, Jewelry Repair, Rolex Watch, San Diego"
META_DESCRIPTION = "Michael Collins Jewelry Store is a well known local jewery store providing custom jewelry and Rolex watch services and jewelry repair"

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'ecomstore.utils.context_processors.ecomstore',
)
GOOGLE_CHECKOUT_MERCHANT_ID = "708343757821939"
GOOGLE_CHECKOUT_MERCHANT_KEY = "jrPWjh7p7kb5aPdZ29k-Lw"
GOOGLE_CHECKOUT_URL = "https://sandbox.google.com/checkout/api/v2/merchantCheckout/Merchant/"+ GOOGLE_CHECKOUT_MERCHANT_ID
CACHE_TIMEOUT = 60 * 60

AUTHNET_POST_URL = 'test.authorize.net'
AUTHNET_POST_PATH = '/gateway/transact.dll'
AUTHNET_LOGIN = '8gXZ497Qxd'
AUTHNET_KEY = '238TVfjA4E6Eh3tg'
AUTH_PROFILE_MODULE = 'accounts.userprofile'

PRODUCTS_PER_PAGE = 12

