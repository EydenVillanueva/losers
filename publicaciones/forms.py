from django.forms import ModelForm
from django import forms
from .models import Publicacion

class PublicacionForm(ModelForm):
    
    class Meta:
        model = Publicacion
        fields = ['nombre','contenido','imagen_fondo']