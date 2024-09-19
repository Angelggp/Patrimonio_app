from django.contrib import admin
from .models import Maestria, Doctorado, Catedra

# Register your models here.
admin.site.register(Maestria)
admin.site.register(Doctorado)
admin.site.register(Catedra)