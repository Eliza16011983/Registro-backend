from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework.routers import DefaultRouter
from api.views import UsuarioViewSet  # Asegurate de que este import sea correcto

from django.conf import settings
from django.conf.urls.static import static

def health_check(request):
    return JsonResponse({'status': 'ok'})

# Registrar el ViewSet con el router
router = DefaultRouter()
router.register(r'users', UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check),         # ✅ Endpoint para Kubernetes
    path('api/', include(router.urls)),        # ✅ Rutas de DRF
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # ✅ Archivos estáticos
