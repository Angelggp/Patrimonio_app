from django.contrib import admin

# Register your models here.
from .models import Facultad, AreaFacultad

admin.site.register(Facultad)
admin.site.register(AreaFacultad)