from django.urls import path
from .views import VRegistro, cerra_sesion, login_view

urlpatterns = [
    path('', VRegistro.as_view(), name='autenticacion'),
    path('logout/', cerra_sesion, name='cerrar_sesion'),
    path('login/', login_view, name='login'),
]