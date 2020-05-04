from django.contrib import admin

# Register your models here.
from .models import Habilidades, Empleado, Trabajo

admin.site.register(Habilidades)
admin.site.register(Empleado)
admin.site.register(Trabajo)