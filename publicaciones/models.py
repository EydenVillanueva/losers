from django.db import models

# Create your models here.

class Publicacion(models.Model):
    nombre = models.CharField(max_length=300)
    contenido = models.TextField()
    imagen_fondo = models.FileField()
    fecha = models.DateField()

    def __str__(self):
        return self.nombre
        