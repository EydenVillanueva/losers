from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Publicacion(models.Model):
    nombre = models.CharField(max_length=300)
    contenido = RichTextUploadingField(blank=True,null=True)
    imagen_fondo = models.FileField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
        