import os

### Initialization ###
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE_HEADER = "BZDS Admin Site" # Django administration -> in <h1>
SITE_TITLE = "BZDS Admin Site" # Django site admin -> in <title>
ADMIN_INDEX_TITLE = "Admin Dashboard" # Site administration -> Home Admin Title


### Configurations ###
ROOT_URLCONF = 'bosscha_doublestar_dataquery.urls'
WSGI_APPLICATION = 'bosscha_doublestar_dataquery.wsgi.application'

# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True

# SECURE_HSTS_SECONDS = 0 #Hahh???
# SECURE_SSL_REDIRECT = True #Hahh???


### Application Definition ###
INSTALLED_APPS = [
    # custom
    'data_archive',

    # 3rd party
    'import_export',
    'dbview',

    # built in
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


### Password Validation ###
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


### Internationalization ###
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_L10N = True
USE_TZ = True


### Model AutoField ###
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


### Static Files ###
STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")] # Comment this in production before collectstatic

# STATIC_ROOT = str(os.path.join(BASE_DIR, "static/")) # For production


### LOGOUT URL ###
LOGOUT_REDIRECT_URL = '/'


# DJANGO ADMIN INTERFACE
# X_FRAME_OPTIONS = 'SAMEORIGIN' # only if django version >= 3.0