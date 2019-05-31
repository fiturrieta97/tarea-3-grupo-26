from django.shortcuts import render
from .models import Cliente, Pedido, Proveedor, Insumo, Perdidas, Detalle_Pedido
# Create your views here.
def inicio(request):
    return render(request, 'appT1/inicio.html')

def admin(request):
	return render(request, 'appT1/admin.html')

	
def inventario(request):
	return render(request, 'appT1/inventario.html')
	
def proveedores(request):
    return render(request, 'appT1/proveedores.html')

def tareasArealizar(request):
    return render(request, 'appT1/tareas.html')	



def crearProveedor(request):
	nombre = request.POST['']
	nombre_contacto = request.POST['']
	correo = request.POST['']
	numero = request.POST['']
	rut_empresa =  request.POST['']
	proveedor = Proveedor(nombre= nombre, nombre_contacto= nombre_contacto, correo= correo, numero=numero, rut_empresa= rut_empresa)
	proveedor.save()
	return render(request, 'appT1/added_proveedor.html')


def form_actualizar_proveedor(request):
	correo_provider = request.POST['']
	context = {}
	context['proveedor'] = Proveedor.objects.filter(correo = correo_provider)
	return render(request, 'appT1/update_proveedor.html')

def actualizar_proveedor(request):
	new_nombre = request.POST['']
	new_nombre_contacto = request.POST['']
	new_correo = request.POST['']
	new_numero = request.POST['']
	new_rut_empresa = request.POST['']
	proveedor = Proveedor.objects.filter(nombre= new_nombre)
	proveedor.nombre = new_nombre
	proveedor.nombre_contacto = new_nombre_contacto
	proveedor.correo = new_correo
	proveedor.numero = new_numero
	proveedor.rut_empresa = new_rut_empresa
	proveedor.save()
	return redirect('proveedores')


def eliminar_proveedor(request):
	nombre_proveedor = request.POST['']
	proveedor = Proveedor.objects.filter(nombre= nombre_proveedor)
	proveedor.delete()
	return redirect('proveedores')

def crearPedido(request):
	pagado = request.POST['']
	medio_pago = request.POST['']
	fecha_pedido = request.POST['']
	trabajador_encargado= request.POST['']
	terminado = request.POST['']
	nombre_cliente = request.POST['']
	cliente = Cliente.objects.get(nombre = nombre_cliente)
	pedido = Pedido(pagado = pagado, medio_pago=medio_pago, fecha_pedido=fecha_pedido, trabajador_encargado=trabajador_encargado, terminado= terminado, cliente=cliente)
	pedido.save()
	return render(request, 'appT1/added_pedido.html')

	actualizar_pedido(request):
	old_cliente = request.POST['']
	cliente = Cliente.objects.get(nombre = old_cliente)
	new_pagado = request.POST['']
	new_medio_pago = request.POST['']
	new_fecha = request.POST['']
	new_trabajador = request.POST['']
	new_terminado =  request.POST['']
	pedido = Pedido.objects.filter(cliente= cliente)
	pedido.pagado = new_pagado
	pedido.medio_pago = new_medio_pago
	pedido.fecha_pedido = new_fecha
	pedido.trabajador_encargado = new_trabajador
	pedido.terminado = new_terminado
	pedido.save()
	return redirect('pedidos')


def crearCliente(request):
	nombre = request.POST['']
	correo = request.POST['']
	rut = request.POST['']
	nombre_empresa = request.POST['']
	numero = request.POST['']
	cliente = Cliente(nombre=nombre, correo=correo, rut=rut, nombre_empresa=nombre_empresa, numero=numero)
	cliente.save()
	return render(request, 'appT1/added_cliente.html')

def form_actualizar_cliente(request):
	correo_cliente = request.POST['']
	context = {}
	context['cliente'] = Cliente.objects.filter(correo = correo_cliente)
	return render(request, 'appT1/update_cliente.html')

def actualizar_cliente(request):
	new_nombre = request.POST['']
	new_correo = request.POST['']
	new_rut = request.POST['']
	new_nombre_empresa = request.POST['']
	new_numero = request.POST['']
	cliente = Cliente.objects.filter(correo=correo_cliente)
	cliente.nombre = new_nombre
	cliente.correo = new_correo
	cliente.rut = new_rut
	cliente.nombre_empresa = new_nombre_empresa
	cliente.numero = new_numero
	cliente.save()
	return redirect('clientes')

def eliminar_cliente(request):
	nombre_cliente = request.POST['']
	cliente = Cliente.objects.filter(nombre= nombre_cliente)
	cliente.delete()
	return redirect('clientes')


def crearInsumo(request):
	nombre = request.POST['']
	dimensiones = request.POST['']
	color = request.POST['']
	stock = request.POST['']
	precio = request.POST['']
	nombre_proveedor = request.POST['']
	proveedor = Proveedor.objects.get(nombre= nombre_proveedor)
	insumo = Insumo(nombre= nombre, dimensiones= dimensiones, color= color, stock = stock, precio = precio, proveedor = proveedor)
	insumo.save()
	return render(request, 'appT1/added_insumo.html')

def form_actualizar_Insumo(request):
	correo_provider = request.POST['']
	context = {}
	context['proveedor'] = Proveedor.objects.filter(correo = correo_provider)
	return render(request, 'appT1/update_proveedor.html')

def actualizar_insumo(request):
	nombre_anterior = request.POST['nombre_anterior']
	insumo = Insumo.objects.filter(nombre= nombre_anterior)
	insumo.stock = request.POST['nuevo_stock']
	insumo.precio = request.POST['nuevo_precio']
	insumo.proveedor = request.POST['nuevo_proveedor']
	insumo.save()
	return redirect('insumos')


