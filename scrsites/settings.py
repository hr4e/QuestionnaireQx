# Django settings for scrsites project.
import socket

DEBUG = True
DEBUG_1 = True
RUN_UNDER_WSGI = False
REQUIRE_LOGIN = True
TEMPLATE_DEBUG = DEBUG

if socket.gethostname() == 'screengenes.org' or RUN_UNDER_WSGI:
	WSGI_URL_PREFIX = '/scrntest/' # required when running under wsgi
else:
	WSGI_URL_PREFIX = '/' # required when running the development server

# User login authentication
# Login URL
LOGIN_URL = WSGI_URL_PREFIX + 'multiquest/registration/login/'
# redirect after login
LOGIN_REDIRECT_URL = WSGI_URL_PREFIX + 'multiquest/registration/userLanding/'

ADMINS = (
	('Screener admin', 'Screener@screengenes.org'),
	)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'djdb',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'djuser',
        'PASSWORD': 'dingo23dog',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
	'.screengenes.org',
	'screengenes.org.',
	'50.79.41.36',
	'50.79.41.35',
	'50.79.41.33',
	'localhost',
	]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Los_Angeles'

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
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
import os.path
MEDIA_ROOT = '/Users/cl/Documents/DjCode/scrsites/images'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = 'http://screengenes.org/screener/images/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = 'http://screengenes.org/screener/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = ')cov_if+h03fo=9&y6zsqvf64x+@q*f+(h!k@bt_890qsk+x6n'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_EXPIRE_AT_AGE = 3600	# expires in ... seconds of age
SESSION_COOKIE_NAME = 'Screener'

ROOT_URLCONF = 'scrsites.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'scrsites.wsgi.application'

import os.path
TEMPLATE_DIRS = (
	os.path.join(os.path.dirname(__file__),'templates').replace('\\','/'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'scrsites.books',
    'scrsites.contact',
    'polls',
    'polls2',
    'multiquest',
    'sudoku',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'scrsites',
)
# Email setup
EMAIL_HOST = 'smtpout.secureserver.net'
EMAIL_HOST_PASSWORD = 'mixed25message'
EMAIL_HOST_USER = 'Screener@screengenes.org'
EMAIL_PORT = 25
EMAIL_SUBJECT_PREFIX = 'Screener'
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'screener@screengenes.org'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

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
