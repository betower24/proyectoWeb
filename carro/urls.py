from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name="carro"
urlpatterns = [
    
    path("agregar/<int:producto_id>/", views.agregar_prod, name="agregar"),
    path("eliminar/<int:producto_id>/", views.eliminar_prod, name="eliminar"),
    path("restar/<int:producto_id>/", views.restar_prod, name="restar"),
    path("limpiar/", views.limpiar_car, name="limpiar"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)