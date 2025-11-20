from django.contrib import admin
from .models import Pedido, LineaPedido  # Corrected LineaP to LineaPedido

admin.site.register(Pedido)
admin.site.register(LineaPedido)