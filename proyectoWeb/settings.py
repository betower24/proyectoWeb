from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# Variables de entorno
# -----------------------------
SECRET_KEY = os.environ.get("SECRET_KEY", "insecure-key")
DEBUG = os.environ.get("DEBUG", "False") == "True"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

# Para evitar errores CSRF en Vercel
CSRF_TRUSTED_ORIGINS = ["https://*.vercel.app", "https://tu-dominio.com"]  # agrega tu dominio si tienes

# -----------------------------
# Apps
# -----------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "proyectoWebApp",
    "servicios",
    "blog",
    "contacto",
    "tienda",
    "carro",
    "autenticacion",
    "pedidos",

    "crispy_forms",
    "crispy_bootstrap4",
]

CRISPY_TEMPLATE_PACK = "bootstrap4"

# -----------------------------
# MIDDLEWARE (¡SOLO UNA VEZ! y en el orden correcto)
# -----------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",          # ← justo después de SecurityMiddleware
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "proyectoWeb.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "carro.context_processors.importe_total_carro",
            ],
        },
    },
]

WSGI_APPLICATION = "proyectoWeb.wsgi.application"

# -----------------------------
# Base de datos
# -----------------------------
import os
import dj_database_url

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.config(default=DATABASE_URL)
    }
else:
    # Usa SQLite en memoria o archivo temporal si no hay DATABASE_URL (ideal para Vercel)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "/tmp/db.sqlite3",  # Vercel permite escribir en /tmp
        }
    }

# -----------------------------
# Archivos estáticos y media (OBLIGATORIO EN VERCEL)
# -----------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Esto hace que WhiteNoise sirva también los media en producción (muy útil en Vercel)
STATICFILES_DIRS = [BASE_DIR / "static"]  # si tienes carpeta static/ adicional

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ← LÍNEA MÁGICA QUE SIRVE MEDIA EN PRODUCCIÓN CON WHITENOISE
WHITENOISE_MANIFEST_STRICT = False
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# -----------------------------
# Email y el resto (lo dejaste bien)
# -----------------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

LANGUAGE_CODE = "es-MX"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"