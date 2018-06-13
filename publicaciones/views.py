from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def nueva_publicacion(request):

    return render(request, 'nueva_publicacion.html', {})

