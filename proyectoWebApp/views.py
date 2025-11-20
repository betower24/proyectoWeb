from django.shortcuts import render
from servicios.models import Servicios  # Cambia a mayúscula

def home(request):
    return render(request, "proyectoWebApp/home.html")






