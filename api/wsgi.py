import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyectoWeb.settings')
application = get_wsgi_application()

# ESTA LÍNEA ES LA QUE VER CEL BUSCA → ¡¡OBLIGATORIA!!
app = application