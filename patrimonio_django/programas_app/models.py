from django.db import models
from facultad_app.models import Facultad

# Create your models here.
class Maestria(models.Model):
    nombre_maestria = models.CharField(max_length=100)
    coordinador = models.CharField(max_length=100)  # Coordinador puede ser nulo
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    excelencia = models.BooleanField(default=False)  # True/False
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_maestria

class Doctorado(models.Model):
    nombre_doctorado = models.CharField(max_length=100)
    coordinador = models.CharField(max_length=100)  # Coordinador puede ser nulo
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    excelencia = models.BooleanField(default=False)  # True/False
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_doctorado
    
class Catedra(models.Model):
    nombre_catedra = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_catedra