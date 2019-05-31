from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='/'),
    path('admin', views.admin, name='/admin'),
    path('inventario', views.inventario, name='/inventario'),
    path('proveedores', views.proveedores, name='/proveedores'),
    path('pedidos', views.pedidos, name='/pedidos'),
    path('lista_clientes', views.lista_clientes, name='/lista_clientes'),
    path('cotizacion', views.cotizacion, name='/cotizacion'),

]


