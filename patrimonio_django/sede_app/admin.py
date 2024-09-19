from django.contrib import admin

# Register your models here.
from .models import Sede, AreaSede

admin.site.register(Sede) 
admin.site.register(AreaSede)