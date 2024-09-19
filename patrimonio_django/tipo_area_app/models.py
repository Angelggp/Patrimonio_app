from django.db import models

# Create your models here.
class TipoArea(models.Model):
    nombre_tipo_area = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_tipo_area