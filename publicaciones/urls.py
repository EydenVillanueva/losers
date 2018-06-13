from django.urls import path
from . import views

app_name ="publicaciones"

urlpatterns = [
    path('nueva/', views.nueva_publicacion,name="nueva"),
]
