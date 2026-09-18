import os

from .base import *

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = True

ALLOWED_HOSTS = [
    host.strip() for host in os.environ["ALLOWED_HOSTS"].split(",") if host.strip()
]

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(",")
    if origin.strip()
]


CSRF_COOKIE_SECURE = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

USE_X_FORWARDED_HOST = True


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


STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "access_key": os.environ["B2_APPLICATION_KEY_ID"],
            "secret_key": os.environ["B2_APPLICATION_KEY"],
            "bucket_name": os.environ["B2_BUCKET_NAME"],
            "endpoint_url": os.environ["B2_ENDPOINT_URL"],
            "region_name": os.environ["B2_REGION"],
            "default_acl": None,
            "querystring_auth": False,
        },
    },
    "staticfiles": {
        "BACKEND": ("whitenoise.storage.CompressedManifestStaticFilesStorage"),
    },
}


STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = f"{os.environ['B2_ENDPOINT_URL']}/" f"{os.environ['B2_BUCKET_NAME']}/media/"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = os.environ["BREVO_HOST"]
EMAIL_PORT = int(os.environ.get("BREVO_PORT", "587"))

EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.environ["BREVO_SMTP_LOGIN"]
EMAIL_HOST_PASSWORD = os.environ["BREVO_SMTP_PASSWORD"]

DEFAULT_FROM_EMAIL = os.environ["WEBSITE_EMAIL"]
SERVER_EMAIL = os.environ["WEBSITE_EMAIL"]

WAGTAILADMIN_BASE_URL = os.environ["WAGTAILADMIN_BASE_URL"]
