from django.contrib import admin
from .models import Socio

class SocioAdmin(admin.ModelAdmin):
    list_display = ('rut','nombre','apellidop','apellidom','direccion','comuna','telefono','correo','region','contrasena')
    search_fields = ('nombre', 'rut')
 

admin.site.register(Socio, SocioAdmin)


