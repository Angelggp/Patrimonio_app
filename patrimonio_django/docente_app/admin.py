from django.contrib import admin

# Register your models here.
from .models import Docente, DocenteFacultad, DocenteSede, Cargo # Importa tu modelo

admin.site.register(Docente)
admin.site.register(DocenteFacultad)
admin.site.register(DocenteSede)
admin.site.register(Cargo)