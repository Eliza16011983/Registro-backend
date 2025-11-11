# Backend - Registro de Usuarios

Este módulo implementa la lógica del backend para el sistema de registro de usuarios. Expone una API REST para gestionar usuarios y enviar notificaciones.

## Tecnologías
- Python 3
- Django
- SQLite (solo para desarrollo)
- Gunicorn (para producción)
- Docker

## Endpoints principales
- `POST /api/usuarios/`: registrar nuevo usuario
- `GET /api/usuarios/`: listar usuarios registrados

## Configuración
1. Crear entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

2.Instalar dependencias:
pip install -r requirements.txt

3.Ejecutar servidor:
python manage.py runserver

Producción

    Se incluye configuración para Gunicorn y Docker.

    Verificar que .env contenga las variables necesarias.

Notas

    El backend se comunica con el microservicio de notificaciones vía HTTP.
