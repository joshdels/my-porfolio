import os

from .base import *

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = False


ALLOWED_HOSTS = [
    host.strip() for host in os.environ["ALLOWED_HOSTS"].split(",") if host.strip()
]


# PostgreSQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.environ["POSTGRES_HOST"],
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}


# Backblaze B2 / S3
AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]

AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]

AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]

AWS_S3_ENDPOINT_URL = os.environ["AWS_S3_ENDPOINT_URL"]

AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME")

AWS_S3_SIGNATURE_VERSION = "s3v4"

AWS_S3_FILE_OVERWRITE = False

AWS_DEFAULT_ACL = None

AWS_QUERYSTRING_AUTH = False


# Static files
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "location": "media",
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "location": "static",
        },
    },
}


STATIC_URL = (
    f"{os.environ['AWS_S3_ENDPOINT_URL']}/"
    f"{os.environ['AWS_STORAGE_BUCKET_NAME']}/static/"
)

MEDIA_URL = (
    f"{os.environ['AWS_S3_ENDPOINT_URL']}/"
    f"{os.environ['AWS_STORAGE_BUCKET_NAME']}/media/"
)


# Wagtail
WAGTAILADMIN_BASE_URL = os.environ["WAGTAILADMIN_BASE_URL"]


# CSRF
CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(",")
    if origin.strip()
]


# Security
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 31536000

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True
