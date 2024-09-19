from django.db import models

# Create your models here.
class Sede(models.Model):
    nombre_sede = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    historia = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_sede
    
class AreaSede(models.Model):
    nombre_area = models.CharField(max_length=100)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, related_name='areas')
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_area