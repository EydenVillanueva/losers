from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse

from .forms import PublicacionForm
from .models import Publicacion
# Create your views here.

def nueva_publicacion(request):

    form = PublicacionForm(request.POST or None,request.FILES)

    if(form.is_valid()):
        publicacion = form.save()
        form = PublicacionForm()
        publicacion.save()

    return render(request, 'nueva_publicacion.html', {'form':form})

'''
def editar_publicacion(request):

    return HttpResponse("Editando Publicacion")
'''

def ver_publicacion(request,id_publicacion):    

    publicacion = Publicacion.objects.get(pk=id_publicacion)

    return render(request,'ver_publicacion.html',{'publicacion':publicacion})
    #return render_to_response('ver_publicacion.html',{'publicacion':publicacion})
