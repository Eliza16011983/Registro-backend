import os
import requests

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Usuario
from .serializers import UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        print("📩 Recibí el POST en /users/")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usuario = serializer.save()
        print("✅ Usuario creado:", serializer.data)

        # 🔥 NOTIFICACIÓN AL MICROSERVICIO
        notify_url = os.environ.get("NOTIFICATION_URL")
        if notify_url:
            try:
                response = requests.post(
                    notify_url,
                    json={
                        "evento": "usuario_creado",
                        "nombre": usuario.nombre,
                        "email": usuario.email,
                        "telefono": usuario.telefono,
                    },
                    timeout=3,
                )
                print("📤 Notificación enviada -> status:", response.status_code)
            except Exception as e:
                print("⚠️ Error al enviar notificación:", str(e))
        else:
            print("⚠️ NOTIFICATION_URL no está configurada")

        return Response(serializer.data, status=status.HTTP_201_CREATED)
