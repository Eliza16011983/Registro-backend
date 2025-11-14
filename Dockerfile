# Imagen base oficial de Python
FROM python:3.10-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements.txt primero
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . /app

# ✅ Recolectar archivos estáticos (DRF, admin, etc.)
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Lanzar Gunicorn con timeout extendido
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "1", "--timeout", "120", "--log-level", "info"]
