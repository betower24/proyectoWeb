# tienda/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda, name='tienda'),  # Asumiendo que tienes una vista "tienda"
]