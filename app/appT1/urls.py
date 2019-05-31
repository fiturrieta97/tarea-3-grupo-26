from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio, name='Inicio'),
    path('sesion', views.sesion, name='sesion'),
    path('Inicio', views.Inicio, name='Inicio'),
    path('inventario', views.inventario, name='inventario'),
    path('proveedores', views.proveedores, name='proveedores'),
    path('tareas', views.tareasArealizar, name='tareas'),



]


