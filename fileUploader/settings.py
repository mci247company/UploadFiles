import os
import socket

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY', 'gx)q!%#ddqj+cnu5x4-a4m+4leq==8sf176a$_(u83$1t&1uj6')
DEBUG = True

# Check whether website in development or production statge
PRODUCTION_SERVERS = ['ip-172-31-47-54', 'vps-22-09-16-11-11-39-180']
print(socket.gethostname())

def check_env():
    for item in PRODUCTION_SERVERS:
        match = item == socket.gethostname()
        if match:
            return True

if check_env():
    PRODUCTION = True
else:
    PRODUCTION = False

print(PRODUCTION)

if PRODUCTION:
    ALLOWED_HOSTS = ["beta.mcivietnam.com", "www.beta.mcivietnam.com", 
    "tiep.mcivietnam.com", "www.tiep.mcivietnam.com"]
else:
    ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'uploader',
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

ROOT_URLCONF = 'fileUploader.urls'

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

WSGI_APPLICATION = 'fileUploader.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
# thay đổi phụ thuộc vào debug mode - Tiệp
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'

# Save media files on Amazon S3 Storage, note media file only
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_ACCESS_KEY_ID = 'AKIA2FGO6GPYGB7YW6FY'
AWS_S3_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = "publicmci"
AWS_QUERYSTRING_AUTH = False

# Streaming video rather play video using AWS CloudFront rather than S3 Storage
AWS_CLOUDFRONT_DOMAIN_NAME = 'd1t3tl7nn69wlp.cloudfront.net'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_CLOUDFRONT_DOMAIN_NAME}'
