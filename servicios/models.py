from django.db import models

class Servicios(models.Model):
    titulo = models.CharField(max_length=100)  # Aumenté el tamaño
    contenido = models.TextField()  # Cambié a TextField para más espacio
    imagen = models.ImageField(upload_to='servicios/', null=True, blank=True)  # Ruta más clara
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'servicio'  # Singular
        verbose_name_plural = 'servicios'  # Plural

    def __str__(self):
        return self.titulo