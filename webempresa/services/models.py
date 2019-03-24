from django.db import models

# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=200,verbose_name="Título")
    subtitle = models.CharField(max_length=200,verbose_name="Subtítulo")
    content = models.TextField(verbose_name="contenido")
    image = models.ImageField(verbose_name="Imagen",upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha cración")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name= "Servicio"
        verbose_name_plural= "Servicios"
        ordering = ["-created"]
    def __str__(self):
        return self.title