import os
import dj_database_url
import django_heroku

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = os.environ['SECRET_KEY']


DEBUG = False



# ALLOWED_HOSTS = [
#                  os.environ['ALLOWED_HOST_1'],
#                  os.environ['ALLOWED_HOST_2'],
#                  os.environ['ALLOWED_HOST_3']
#                 ]

ALLOWED_HOSTS = [os.environ['ALLOWED_HOST_1']]

ADMINS = (
    ("Pius Lucky", os.environ['ADMIN_EMAIL']),
)

DOMAIN_NAME = os.environ['DOMAIN_NAME']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages', 
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'cloudinary_storage',
    'cloudinary',
    'django.contrib.staticfiles',
    'django.contrib.redirects',
    # third-party apps
    'froala_editor',
    'pwa',
    'robots',
    # apps
    'central',
    'authorize',
]

ROBOTS_USE_SCHEME_IN_HOST = True

ROBOTS_SITEMAP_URLS = [
    os.environ['SITEMAP_URL']
]

SITE_ID = int(os.environ['SITE_ID'])

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, os.environ['PWA_SERVICE_WORKER_PATH'])

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django.middleware.gzip.GZipMiddleware",
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware'
]

ROOT_URLCONF = 'jap.urls'

TEMPLATES = [
    {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [ os.path.join(BASE_DIR, 'templates')],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'central.context_processors.major_data',
            'central.context_processors.pagination_data'
        ],
    },
    },
]

WSGI_APPLICATION = 'jap.wsgi.application'


# DATABASES = {
#     'default': {
#         'ENGINE': os.environ['DATABASE_ENGINE'],
#         'NAME': os.environ['DATABASE_NAME'],
#         'USER': os.environ['DATABASE_USER'],
#         'PASSWORD': os.environ['DATABASE_USER_PASSWORD'],
#         'HOST': os.environ['DATABASE_HOST'],
#         'PORT': os.environ['DATABASE_PORT']
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


CSRF_FAILURE_VIEW = "central.views.csrf_byepass"


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = int(os.environ['EMAIL_PORT'])
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
DEFAULT_FROM_EMAIL = os.environ['DEFAULT_FROM_EMAIL']


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'authorize.email_auth.EmailAuthBackend',
)


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True



LOGOUT_REDIRECT_URL = "/"


django_heroku.settings(locals())

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)



CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ['CLOUDINARY_CLOUD_NAME'],
    'API_KEY': os.environ['CLOUDINARY_API_KEY'],
    'API_SECRET': os.environ['CLOUDINARY_API_SECRET'],
}


MEDIA_URL = '/media/'

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

STATIC_ROOT = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'staticfiles'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


# Securing site
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
