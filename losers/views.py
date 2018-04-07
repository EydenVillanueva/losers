from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from publicaciones.models import Publicacion
from django.core.mail import send_mail
from .forms import FormContacto

def index(request):
    return HttpResponse("Hola Mundo")

def contacto(request):
    
    formulario = FormContacto(request.POST or None)

    if formulario.is_valid():

        correo = formulario.cleaned_data.get('correo')
        mensaje = formulario.cleaned_data.get('mensaje')
        nombre = formulario.cleaned_data.get('nombre')

        correo_mensaje = '%s: %s enviado por %s' %(nombre, mensaje, correo)

        send_mail(
            nombre,
            correo_mensaje,
            correo,
            ['pedroesparzaaa@gmail.com'],
            fail_silently=False,
        )
    
    formulario = FormContacto()

    contexto = {'formulario': formulario}

    return render(request, 'contacto.html',contexto)
        
