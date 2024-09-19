from django.db import models
from facultad_app.models import AreaFacultad
from sede_app.models import AreaSede

# Create your models here.

class Cargo(models.Model):
    nombre_cargo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_cargo
    
class Docente(models.Model):
    nombre_docente = models.CharField(max_length=100)
    apellido_docente = models.CharField(max_length=100)
    ci = models.CharField(max_length=20)  # Cédula de Identidad
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    fecha_alta = models.DateField()
    fecha_baja = models.DateField(blank=True, null=True)  # Puede ser nulo si el docente está activo
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_docente} {self.apellido_docente}"
    
    
class DocenteFacultad(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    area_facultad = models.ForeignKey(AreaFacultad, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('docente', 'area_facultad')  # Asegura que un docente no esté duplicado en el área
        
class DocenteSede(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    area_sede = models.ForeignKey(AreaSede, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('docente', 'area_sede')  # Asegura que un docente no esté duplicado en el área
        
