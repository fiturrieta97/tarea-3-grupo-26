from django.shortcuts import render
from .models import Cliente, Pedido, Proveedor, Insumo, Detalle_Pedido 
# Create your views here.
def inicio(request):
    return render(request, 'appT1/inicio.html')

def admin(request):
	return render(request, 'appT1/admin.html')

def inventario(request):
	contexto={}
	contexto['insumos'] = Insumo.objects.all()
	return render(request, 'appT1/inventario.html', contexto)
	
def proveedores(request):
	contexto={}
	contexto['proveedores'] = Proveedor.objects.all()
	return render(request, 'appT1/proveedores.html', contexto)

def pedidos(request):
    return render(request, 'appT1/pedidos.html')

def lista_clientes(request):
	contexto={}
	contexto['clientes'] = Cliente.objects.all()
	return render(request, 'appT1/lista_clientes.html', contexto)

def cotizacion(request):
    return render(request, 'appT1/cotizacion.html')	

def new_proveedor(request):
	return render(request, 'appT1/new_proveedor.html')

def new_insumo(request):
    contexto={}
    contexto['proveedores'] = Proveedor.objects.all()
    return render(request, 'appT1/new_insumo.html', contexto)

def update_insumo(request):
    contexto={}
    contexto['proveedores'] = Proveedor.objects.all()
    return render(request, 'appT1/update_insumo.html', contexto)

def new_pedido(request):
    contexto={}
    contexto['clientes'] = Cliente.objects.all()
    return render(request, 'appT1/new_pedido.html', contexto)

def new_cliente(request):
	return render(request, 'appT1/new_cliente.html')

def crear_proveedor(request):
	nombre = request.POST['nombre_proveedor']
	nombre_contacto = request.POST['nombre_contacto']
	correo = request.POST['correo']
	numero = request.POST['numero']
	rut_empresa =  request.POST['rut']
	proveedor = Proveedor(nombre= nombre, nombre_contacto= nombre_contacto, correo= correo, numero=numero, rut_empresa= rut_empresa)
	proveedor.save()
	context = {'form':'¡Proveedor añadido con éxito!','nombre':nombre, 'nombre_contacto':nombre_contacto, 'correo':correo, 'numero':numero, 'rut':rut_empresa}
	return render(request, 'appT1/added_proveedor.html', context)


def actualizar_proveedor(request):
	old_name = request.POST['']
	new_nombre_contacto = request.POST['']
	new_correo = request.POST['']
	new_numero = request.POST['']
	new_rut_empresa = request.POST['']
	proveedor = Proveedor.objects.filter(nombre= old_name)
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

def crear_pedido(request):
	id_pedido = len(Pedido.objects.all())
	pagado = request.POST['']
	medio_pago = request.POST['']
	fecha_pedido = request.POST['']
	trabajador_encargado= request.POST['']
	terminado = request.POST['']
	nombre_cliente = request.POST['']
	cliente = Cliente.objects.get(nombre = nombre_cliente)
	pedido = Pedido(pagado = pagado, medio_pago=medio_pago, fecha_pedido=fecha_pedido, trabajador_encargado=trabajador_encargado, terminado= terminado, cliente=cliente)
	pedido.save()
	context = {'form':'¡Pedido añadido con éxito!','medio_pago':medio_pago, 'fecha_pedido':fecha_pedido, 'trabajador_encargado':trabajador_encargado, 'terminado':terminado, 'cliente':cliente}
	return render(request, 'appT1/added_pedido.html', context)

def actualizar_pedido(request):
	id_pedido = request.POST['']
	cliente = Cliente.objects.get(id_pedido = id_pedido)
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


def crear_cliente(request):
	nombre = request.POST['nombre_cliente']
	correo = request.POST['correo']
	rut = request.POST['rut']
	nombre_empresa = request.POST['nombre_empresa']
	numero = request.POST['numero']
	cliente = Cliente(nombre=nombre, correo=correo, rut=rut, nombre_empresa=nombre_empresa, numero=numero)
	cliente.save()
	context = {'form':'¡Cliente añadido con éxito!','nombre':nombre,'rut':rut, 'nombre_empresa':nombre_empresa, 'numero':numero}
	return render(request, 'appT1/added_cliente.html', context)


def actualizar_cliente(request):
	old_nombre = request.POST['nombre_cliente']
	new_correo = request.POST['correo']
	new_rut = request.POST['rut']
	new_nombre_empresa = request.POST['nombre_empresa']
	new_numero = request.POST['numero']
	cliente = Cliente.objects.filter(nombre= old_nombre)
	cliente.correo = new_correo
	cliente.rut = new_rut
	cliente.nombre_empresa = new_nombre_empresa
	cliente.numero = new_numero
	cliente.save()
	return redirect('lista_clientes')

def eliminar_cliente(request):
	nombre_cliente = request.POST['']
	cliente = Cliente.objects.filter(nombre= nombre_cliente)
	cliente.delete()
	return redirect('lista_clientes')


def crear_insumo(request):
	nombre = request.POST['nombre']
	dimensiones = request.POST['dimensiones']
	color = request.POST['color']
	stock = request.POST['stock']
	precio = request.POST['precio']
	nombre_proveedor = request.POST['proveedor']
	proveedor = Proveedor.objects.get(nombre= nombre_proveedor)
	insumo = Insumo(nombre= nombre, dimensiones= dimensiones, color= color, stock = stock, precio = precio, proveedor = proveedor)
	insumo.save()
	context = {'form':'¡Insumo añadido con éxito!','nombre':nombre, 'dimensiones':dimensiones, 'correo':color, 'stock':stock, 'precio':precio, 'proveedor':proveedor}
	return render(request, 'appT1/added_insumo.html', context)

def actualizar_insumo(request):
	nombre_anterior = request.POST['nombre_insumo']
	insumo = Insumo.objects.filter(nombre= nombre_anterior)
	insumo.stock = request.POST['nuevo_stock']
	insumo.precio = request.POST['nuevo_precio']
	insumo.proveedor = request.POST['nuevo_proveedor']
	insumo.save()
	return redirect('inventario')

def eliminar_insumo(request):
    nombre_insumo = request.POST['']
    insumo = Insumo.objects.filter(nombre= nombre_insumo)
    insumo.delete()
    return redirect('inventario')


