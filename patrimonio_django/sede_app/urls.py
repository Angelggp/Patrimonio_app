from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SedeViewSet

router = DefaultRouter()
router.register(r'sedes', SedeViewSet)  # Registra el ViewSet con la ruta 'sedes'

urlpatterns = [
    path('', include(router.urls)),  # Incluye las rutas del router
]