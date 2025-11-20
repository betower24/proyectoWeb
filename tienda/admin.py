from django.contrib import admin
from .models import CategoriaProd, Producto

# Register your models here.
class CategoriaPAdmin(admin.ModelAdmin):  # Corrección 1: Nombre de clase
    readonly_fields = ('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):    # Corrección 2: Nombre de clase
    readonly_fields = ('created', 'updated')

admin.site.register(CategoriaProd, CategoriaPAdmin)  # Corrección 3: Orden y nombres
admin.site.register(Producto, ProductoAdmin)         # Corrección 4: Orden y nombres