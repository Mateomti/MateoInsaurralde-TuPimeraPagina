from django.contrib import admin
from django.urls import path
from inicio.views import inicio, registro, listado

urlpatterns = [
    path('', inicio, name='inicio'),
    path('registro/', registro, name='registro'),
    path('listado/', listado, name='listado')
]