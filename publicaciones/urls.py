from django.urls import path, re_path
from . import views

app_name ="publicaciones"

urlpatterns = [
    path('nueva/', views.nueva_publicacion,name="nueva"),
    #re_path(r'^(?P<pk>[0-9]+)/$', views.ver_publicacion,name="ver_publicacion"),
    path('<int:id_publicacion>/', views.ver_publicacion ,name="ver_publicacion"),
    #path('editar/<int:publicacion_id>',views.editar_publicacion,name="editar"),
]
