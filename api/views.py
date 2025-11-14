from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Usuario
from .serializers import UsuarioSerializer
from .notifications import send_user_created_email

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

        try:
            send_user_created_email(usuario)
            print("📤 Correo enviado a:", usuario.email)
        except Exception as e:
            print("⚠️ Error al enviar correo:", str(e))

        return Response(serializer.data, status=status.HTTP_201_CREATED)

