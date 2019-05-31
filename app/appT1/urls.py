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
    path('new_proveedor', views.new_proveedor, name='/new_proveedor'),
    path('crear_proveedor', views.crear_proveedor, name='/crear_proveedor'),
    #path('actualizar_proveedor', views.actualizar_proveedor, name='/actualizar_proveedor'),
    #path('eliminar_proveedor', views.eliminar_proveedor, name='/eliminar_proveedor'),
    path('new_insumo', views.new_insumo, name='/new_insumo'),
    path('crear_insumo', views.crear_insumo, name='/crear_insumo'),
    path('actualizar_insumo', views.actualizar_insumo, name='/actualizar_insumo'),
    #path('eliminar_insumo', views.eliminar_insumo, name='/eliminar_insumo'),
    path('new_cliente', views.new_cliente, name='/new_cliente'),
    path('crear_cliente', views.crear_cliente, name='/crear_cliente'),
    #path('actualizar_cliente', views.actualizar_cliente, name='/actualizar_cliente'),
    #path('eliminar_cliente', views.eliminar_cliente, name='/eliminar_cliente'),
    path('update_insumo', views.update_insumo, name='/update_insumo')



]


