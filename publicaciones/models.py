from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.

class Publicacion(models.Model):
    nombre = models.CharField(max_length=300)
    contenido = RichTextField(('Contenido de Entrada'))
    imagen_fondo = models.FileField()
    fecha = models.DateField()

    def __str__(self):
        return self.nombre
        