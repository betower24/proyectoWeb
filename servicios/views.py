from django.shortcuts import render
from servicios.models import Servicios  # Cambia a mayúscula


# Create your views here.
def servicios(request):
    lista_servicios = Servicios.objects.all()  # Usa una variable más descriptiva
    return render(request, "servicios/servicios.html", {'servicios': lista_servicios}) 