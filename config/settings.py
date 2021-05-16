import os
import sys
from pathlib import Path

from django.core.management.utils import get_random_secret_key

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = bool(os.environ.get("DEBUG", False))
SECRET_KEY = os.environ.get("SECRET_KEY", get_random_secret_key())
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "127.0.0.1 0.0.0.0 localhost").split(
    " "
)

INSTALLED_APPS = [
    "rest_framework",
    "drf_spectacular",
    "backmarker",
]

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": [],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "DEFAULT_SCHEMA_CLASS": "config.openapi.AutoSchema",
    "PAGE_SIZE": 25,
    "UNAUTHENTICATED_USER": None,
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Backmarker REST API",
    "DESCRIPTION": "A basic REST API for F1 data.",
    "VERSION": "0.1.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SCHEMA_PATH_PREFIX": "/api",
}

if DEBUG:
    # For django-rest-framework stylesheets, etc.
    INSTALLED_APPS += ["django.contrib.staticfiles"]
    # Browsable API for debugging
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] += (  # type: ignore
        "rest_framework.renderers.BrowsableAPIRenderer",
    )

MIDDLEWARE = ["django.middleware.security.SecurityMiddleware"]
ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
    }
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ.get("DATABASE_HOST", "localhost"),
        "PORT": int(os.environ.get("DATABASE_PORT", 5432)),
        "NAME": os.environ.get("DATABASE_NAME", "postgres"),
        "USER": os.environ.get("DATABASE_USER", "postgres"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD", "postgres"),
    }
}

if "test" in sys.argv or "pytest" in sys.argv[0]:
    DATABASES["default"] = {"ENGINE": "django.db.backends.sqlite3"}

TIME_ZONE = "UTC"
USE_I18N = False
USE_L10N = False
USE_TZ = True
STATIC_URL = "/static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
