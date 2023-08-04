from django.contrib import admin
from django.urls import path, include
from .views import indice, acerca, bienvenido,contacto,exito,registro,registrado

urlpatterns = [
    path('',indice,name="indice"),
    path('acerca',acerca,name="acerca"),
    path('bienvenido',bienvenido,name="bienvenido"),
    path('contacto', contacto,name="contacto"),
    path('exito',exito,name="exito"),
      path('registrado',registrado, name='registrado'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/',registro, name='registro'),
    
]
