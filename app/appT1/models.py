from django.db import models

# Create your models here.
class Cliente(models.Model):
	nombre=models.CharField(max_length=45)
	correo=models.CharField(max_length=45)
	rut=models.CharField(max_length=10)
	nombre_empresa=models.CharField(max_length=45)
	numero=models.IntegerField()

class Pedido(models.Model):
	pagado=models.BooleanField(default=False)
	medio_pago=models.CharField(max_length=45)
	fecha_pedido=models.DateField()
	trabajador_encargado=models.CharField(max_length=45)
	terminado=models.BooleanField(default=False)
	cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)

class Proveedor(models.Model):
	nombre=models.CharField(max_length=45)
	nombre_contacto=models.CharField(max_length=45)
	correo=models.CharField(max_length=45)
	numero=models.IntegerField()
	rut_empresa=models.CharField(max_length=10)

class Insumo(models.Model):
	nombre=models.CharField(max_length=45)
	dimensiones=models.CharField(max_length=45)
	color=models.CharField(max_length=45)
	stock=models.IntegerField()
	precio=models.IntegerField()
	proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)

class Perdidas(models.Model):
	cantidad_perdida=models.IntegerField()
	fecha=models.DateField()
	insumo=models.ForeignKey(Insumo,on_delete=models.CASCADE)


class Detalle_Pedido(models.Model):
	pedido=models.ForeignKey(Pedido,on_delete=models.CASCADE)
	insumo=models.ForeignKey(Insumo,on_delete=models.CASCADE)
	cantidad=models.IntegerField()





