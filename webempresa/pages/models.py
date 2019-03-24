from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Pages(models.Model):
    title =  models.CharField(max_length=200,verbose_name="Nombre")
    content =   RichTextField(verbose_name="contenido")
    order = models.SmallIntegerField(verbose_name="orden",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha cración")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    class Meta:
        verbose_name= "página"
        verbose_name_plural= "páginas"
        ordering = ["order","title"]
    def __str__(self):
          return self.title
