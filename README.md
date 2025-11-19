# Backend - Registro de Usuarios

Este microservicio gestiona la lógica del sistema, recibiendo solicitudes desde el frontend y procesando la creación y listado de usuarios.
 La API fue desarrollada en Django y expuesta mediante Gunicorn dentro de un contenedor Docker.

## Tecnologías
- Python 3
- Django
- SQLite (solo para desarrollo)
- Gunicorn (para producción)
- Docker

##Rutas principales
Método          Ruta              Descripción
GET          /api/users/       Lista todos los usuarios
POST         /api/users/       Crea un nuevo usuario


manage.py
users_api/
   models.py
   views.py
   urls.py
k8s/
   deployment.yaml
   service.yaml
Dockerfile


##Flujo de funcionamiento:

1-El usuario completa el formulario en el frontend.


2-El frontend envía una solicitud HTTP al backend.


3-Django procesa la solicitud:


   -valida datos


   -crea registro

   -retorna respuesta JSON


4-Se registra el evento en logs del backend.


5-El backend invoca al servicio de notificaciones (si aplicaba la opción A).


##Comandos de prueba
Crear usuario:

curl -i -X POST \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Demo","email":"demo@demo.com","telefono":"123"}' \
  http://<LB-BACKEND>:8000/api/users/

Listar usuarios:
curl -i http://<LB-BACKEND>:8000/api/users/

Despliegue:
docker build -t backend:latest .
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml




