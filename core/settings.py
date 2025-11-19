import os
from pathlib import Path
from dotenv import load_dotenv
import psycopg2

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'fallback-secret-key')

DEBUG = True

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'api',

    'corsheaders',  # CORS
]

MIDDLEWARE = [
    # CORS PRIMERO
    'corsheaders.middleware.CorsMiddleware',

    # Después lo estándar
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'

# =========================
# 📌 BASE DE DATOS
# =========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'usuarios',
        'USER': 'usuarios',
        'PASSWORD': 'usuarios',
        'HOST': 'usuarios.cxeeocrtzohx.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Montevideo'
USE_I18N = True
USE_TZ = True

# =========================
# 📌 STATIC FILES
# =========================
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =========================
# 📌 Django REST Framework
# =========================
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
}

# =========================
# 📌 Email
# =========================
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
ADMIN_EMAIL = os.getenv('EMAIL_RECEIVER')

# =========================
# 📌 CORS CONFIG — LAB
# =========================

# Para el laboratorio: permitir cualquier origen
CORS_ALLOW_ALL_ORIGINS = True

print("### SETTINGS CARGADOS: CORS_ALLOW_ALL_ORIGINS =", CORS_ALLOW_ALL_ORIGINS)

# =========================
# 📌 Chequeo de Base de Datos (para logs)
# =========================
try:
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME', 'usuarios'),
        user=os.getenv('DB_USER', 'usuarios'),
        password=os.getenv('DB_PASSWORD', 'usuarios'),
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', '5432'),
        connect_timeout=3
    )
    conn.close()
except Exception as e:
    print(f"⚠️ Error de conexión a la base de datos: {e}")
