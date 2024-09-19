from django.db import models
from sede_app.models import Sede

# Create your models here.
class Facultad(models.Model):
    nombre_facultad = models.CharField(max_length=100)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, related_name='facultades')
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    numero_acuerdo = models.CharField(max_length=50, blank=True, null=True)
    historia = models.TextField(blank=True, null=True)
    estado_conservacion = models.CharField(max_length=50, choices=[
        ('bueno', 'Bueno'),
        ('malo', 'Malo'),
        ('regular', 'Regular'),
    ], default='bueno')
    estructura = models.TextField(blank=True, null=True)  # Puedes definir un modelo separado si es necesario
    valores = models.TextField(blank=True, null=True)  # Puedes definir un modelo separado si es necesario
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_facultad
    
    
class AreaFacultad(models.Model):
    nombre_area = models.CharField(max_length=100)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE, related_name='areas')
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_area