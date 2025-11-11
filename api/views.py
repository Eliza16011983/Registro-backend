from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer
from .notifications import send_user_created_email

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def perform_create(self, serializer):
        usuario = serializer.save()
        send_user_created_email(usuario)
