from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Sede
from .serializers import SedeSerializer

class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()  # Obtiene todas las instancias de Sede
    serializer_class = SedeSerializer  # Utiliza el serializador que has creado