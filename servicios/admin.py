from django.contrib import admin
from .models import Servicios

class servicio(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Servicios, servicio)