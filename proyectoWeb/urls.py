from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from autenticacion.views import login_view

# proyectoWeb/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('proyectoWebApp.urls')),
    path('servicios/', include('servicios.urls')),
    path('blog/', include('blog.urls')),
    path('contacto/', include('contacto.urls')),
    path('tienda/', include('tienda.urls')),
    path('carro/', include('carro.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('autenticacion/', include('autenticacion.urls')),
    path('login/', login_view, name='login'),  # Agrega esta línea
]

# Opcional: Para archivos estáticos/multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)