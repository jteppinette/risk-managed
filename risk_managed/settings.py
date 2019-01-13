import ast
import os
from urllib import parse

import dj_database_url

ROOT = os.path.dirname(os.path.abspath(__file__))

DEVELOPMENT = ast.literal_eval(os.environ.get("DEVELOPMENT", "True"))
DEBUG = DEVELOPMENT

LOGIN_REDIRECT_URL = "/dashboard"
LOGIN_URL = "/login"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django_settings_export.settings_export",
            ]
        },
    }
]

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "minio_storage",
    "risk_managed.main",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "risk_managed.urls"

EMAIL_DOMAIN = os.environ.get("SMTP_DOMAIN", "risk-managed.localhost")
EMAIL_HOST = os.environ.get("SMTP_SERVER", "0.0.0.0")
EMAIL_PORT = os.environ.get("SMTP_PORT", 1025)
EMAIL_HOST_PASSWORD = os.environ.get("SMTP_PASSWORD", "")
EMAIL_HOST_USER = os.environ.get("SMTP_LOGIN", "")
EMAIL_USE_TLS = EMAIL_PORT == 587
EMAIL_USE_SSL = EMAIL_PORT == 465

EMAIL_SUBJECT_PREFIX = "[Emergency Contacts] "
SERVER_EMAIL = "alerts@{}".format(EMAIL_DOMAIN)
SUPPORT_EMAIL = "support@{}".format(EMAIL_DOMAIN)
DEFAULT_EMAIL_FROM = SUPPORT_EMAIL
ADMINS = [("Admins", "admins@{}".format(EMAIL_DOMAIN))]
MANAGERS = [("Managers", "mangers@{}".format(EMAIL_DOMAIN))]

DEFAULT_FILE_STORAGE = "minio_storage.storage.MinioMediaStorage"
STORAGE_URL = parse.urlparse(os.environ.get("STORAGE_URL", "http://0.0.0.0:9000"))
MINIO_STORAGE_ACCESS_KEY = os.environ.get("STORAGE_ACCESS_KEY_ID", "access-key-id")
MINIO_STORAGE_SECRET_KEY = os.environ.get("STORAGE_SECRET_ACCESS_KEY", "secret-access-key")
MINIO_STORAGE_MEDIA_BUCKET_NAME = os.environ.get("STORAGE_BUCKET", "storage")
MINIO_STORAGE_ENDPOINT = STORAGE_URL.netloc
MINIO_STORAGE_USE_HTTPS = STORAGE_URL.scheme == "https"
MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = bool(DEVELOPMENT)
MINIO_STORAGE_MEDIA_USE_PRESIGNED = True

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = "static"
STATIC_URL = "/static/"

DATABASES = {
    "default": dj_database_url.config(
        default="postgres://db:secret@0.0.0.0:5432/db",
        conn_max_age=600,
        ssl_require=not DEVELOPMENT,
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

SETTINGS_EXPORT = ["SUPPORT_EMAIL"]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = False
USE_L10N = True
USE_TZ = True
USE_THOUSAND_SEPARATOR = True
NUMBER_GROUPING = 3

SECRET_KEY = os.environ.get("SECRET_KEY", "secret")

SECURE_PROXY_SSL_HEADER = ["HTTP_X_FORWARDED_PROTO", "https"]
ALLOWED_HOSTS = ["*"]
