from appT1.models import Cliente,Pedido,Detalle_Pedido,Insumo,Perdidas,Proveedor

cliente1=Cliente(nombre="Felipe Hernandez",correo="felipehernandez@correo.cl",rut="19841552-9",nombre_empresa="FCFM",numero=994535462)
cliente2=Cliente(nombre="Benjamin Hunfan",correo="benjaminhunfan@correo.cl",rut="19248564-5",nombre_empresa="USACH",numero=983214564)
cliente3=Cliente(nombre="Ignacio Leon",correo="ignacioleon@correo.cl",rut="19845613-6",nombre_empresa="Falabella",numero=963254154)
cliente4=Cliente(nombre="Franco Iturrieta",correo="francoiturrieta.cl",rut="19513515-7",nombre_empresa="Entel",numero=965488755)
cliente5=Cliente(nombre="Juan Gutierrez",correo="juangutierrez@correo.cl",rut="20545618-5",nombre_empresa="VTR",numero=966658724)
cliente6=Cliente(nombre="Sofia Herrera",correo="sofiaherrera@correo.cl",rut="19345678-9",nombre_empresa="Movistar",numero=936215477)
cliente7=Cliente(nombre="Victoria Arce",correo="victoriaarce@correo.cl",rut="20345679-8",nombre_empresa="DIRECTV",numero=996854747)
cliente8=Cliente(nombre="Sebastian Donoso",correo="sebastiandonoso@correo.cl",rut="20514351-1",nombre_empresa="Virgin",numero=944576454)
cliente9=Cliente(nombre="Rodrigo Pizarro",correo="rodrigopizarro@correo.cl",rut="20603540-1",nombre_empresa="Walmart",numero=94132357)
cliente10=Cliente(nombre="Benjamin Hurtado",correo="benjaminhurtado@correo.cl",rut="19477122-8",nombre_empresa="Claro",numero=984816542)
cliente1.save()
cliente2.save()
cliente3.save()
cliente4.save()
cliente5.save()
cliente6.save()
cliente7.save()
cliente8.save()
cliente9.save()
cliente10.save()

pedido1=Pedido(pagado=True,medio_pago="cheque",fecha_pedido="2019-04-03",trabajador_encargado="Luis Orellana",terminado=True,cliente=cliente1)
pedido2=Pedido(pagado=True,medio_pago="efectivo",fecha_pedido="2019-04-03",trabajador_encargado="Luis Orellana",terminado=True,cliente=cliente2)
pedido3=Pedido(pagado=True,medio_pago="transferencia",fecha_pedido="2019-04-05",trabajador_encargado="Luis Orellana",terminado=True,cliente=cliente3)
pedido4=Pedido(pagado=True,medio_pago="transferencia",fecha_pedido="2019-04-03",trabajador_encargado="Luis Orellana",terminado=True,cliente=cliente4)
pedido5=Pedido(pagado=False,medio_pago="transferencia",fecha_pedido="2019-04-07",trabajador_encargado="Luis Orellana",terminado=True,cliente=cliente5)
pedido6=Pedido(pagado=False,medio_pago="transferencia",fecha_pedido="2019-04-06",trabajador_encargado="Luis Orellana",terminado=False,cliente=cliente6)
pedido7=Pedido(pagado=True,medio_pago="transferencia",fecha_pedido="2019-04-05",trabajador_encargado="Luis Orellana",terminado=False,cliente=cliente7)
pedido8=Pedido(pagado=False,medio_pago="cheque",fecha_pedido="2019-04-10",trabajador_encargado="Luis Orellana",terminado=True,cliente=cliente8)
pedido9=Pedido(pagado=True,medio_pago="cheque",fecha_pedido="2019-04-10",trabajador_encargado="Luis Orellana",terminado=True,cliente=cliente9)
pedido10=Pedido(pagado=True,medio_pago="transferencia",fecha_pedido="2019-04-10",trabajador_encargado="Luis Orellana",terminado=True,cliente=cliente10)
pedido11=Pedido(pagado=True,medio_pago="cheque",fecha_pedido="2019-04-20",trabajador_encargado="Luis Orellana",terminado=True,cliente=cliente1)
pedido12=Pedido(pagado=False,medio_pago="cheque",fecha_pedido="2019-04-19",trabajador_encargado="Luis Orellana",terminado=False,cliente=cliente1)
pedido13=Pedido(pagado=False,medio_pago="efectivo",fecha_pedido="2019-04-18",trabajador_encargado="Luis Orellana",terminado=False,cliente=cliente2)
pedido1.save()
pedido2.save()
pedido3.save()
pedido4.save()
pedido5.save()
pedido6.save()
pedido7.save()
pedido8.save()
pedido9.save()
pedido10.save()
pedido11.save()
pedido12.save()
pedido13.save()

proveedor1=Proveedor(nombre="Provedor de Tintas",nombre_contacto="Manuel Tintas",correo="manueltintas@correo.cl",numero=98427648,rut_empresa="95426514-9")
proveedor2=Proveedor(nombre="Provedor de Papel",nombre_contacto="Pedro Paper",correo="pedropaper@correo.cl",numero=998412566,rut_empresa="95741062-6")
proveedor3=Proveedor(nombre="Provedor de Micas",nombre_contacto="Juan Micas",correo="juanmicas@correo.cl",numero=999876588,rut_empresa="64512478-5")
proveedor1.save()
proveedor2.save()
proveedor3.save()


insumo1=Insumo(nombre="Toner Blanco y Negro",dimensiones="1 cartucho",color="B/N",stock=20,precio=15000,proveedor=proveedor1)
insumo2=Insumo(nombre="Toner Color",dimensiones="1 cartucho",color="Color",stock=13,precio=20000,proveedor=proveedor1)
insumo3=Insumo(nombre="Bobina de papel Bond",dimensiones="80 gr, 90x150 cm",color="Blanco",stock=30,precio=7000,proveedor=proveedor2)
insumo3.save()
insumo4=Insumo(nombre="Resma Papel Bond 1",dimensiones="75 gr, 21.6x27.9 cm",color="Blanco",stock=100,precio=1500,proveedor=proveedor2)
insumo5=Insumo(nombre="Resma Papel Bond 2",dimensiones="75 gr, 21.6x33 cm",color="Blanco",stock=97,precio=1500,proveedor=proveedor2)
insumo6=Insumo(nombre="Resma Papel Bond 3",dimensiones="75 gr, 27.9x43.2 cm",color="Blanco",stock=65,precio=1500,proveedor=proveedor2)
insumo7=Insumo(nombre="Resma Papel Bond 4",dimensiones="75 gr, 21x29.7 cm",color="Blanco",stock=88,precio=2000,proveedor=proveedor2)
insumo8=Insumo(nombre="Mica PVC 1",dimensiones="21.6x27.9",color="Azul",stock=1000,precio=100,proveedor=proveedor3)
insumo9=Insumo(nombre="Mica PVC 2",dimensiones="21.6x27.9",color="Humo",stock=590,precio=100,proveedor=proveedor3)
insumo10=Insumo(nombre="Mica PVC 3",dimensiones="21.6x27.9",color="Transparente",stock=307,precio=100,proveedor=proveedor3)
insumo1.save()
insumo2.save()

insumo4.save()
insumo5.save()
insumo6.save()
insumo7.save()
insumo8.save()
insumo9.save()
insumo10.save()




detalle1=Detalle_Pedido(pedido=pedido1,insumo=insumo1,cantidad=1)
detalle2=Detalle_Pedido(pedido=pedido1,insumo=insumo3,cantidad=1)
detalle3=Detalle_Pedido(pedido=pedido2,insumo=insumo2,cantidad=1)
detalle4=Detalle_Pedido(pedido=pedido2,insumo=insumo3,cantidad=1)
detalle5=Detalle_Pedido(pedido=pedido3,insumo=insumo1,cantidad=1)
detalle6=Detalle_Pedido(pedido=pedido3,insumo=insumo4,cantidad=1)
detalle7=Detalle_Pedido(pedido=pedido4,insumo=insumo7,cantidad=1)
detalle8=Detalle_Pedido(pedido=pedido4,insumo=insumo8,cantidad=1)
detalle9=Detalle_Pedido(pedido=pedido5,insumo=insumo6,cantidad=1)
detalle10=Detalle_Pedido(pedido=pedido5,insumo=insumo9,cantidad=1)
detalle11=Detalle_Pedido(pedido=pedido6,insumo=insumo6,cantidad=1)
detalle12=Detalle_Pedido(pedido=pedido6,insumo=insumo9,cantidad=1)
detalle13=Detalle_Pedido(pedido=pedido7,insumo=insumo2,cantidad=1)
detalle14=Detalle_Pedido(pedido=pedido7,insumo=insumo5,cantidad=1)
detalle15=Detalle_Pedido(pedido=pedido8,insumo=insumo2,cantidad=1)
detalle16=Detalle_Pedido(pedido=pedido8,insumo=insumo6,cantidad=1)
detalle17=Detalle_Pedido(pedido=pedido9,insumo=insumo2,cantidad=1)
detalle18=Detalle_Pedido(pedido=pedido9,insumo=insumo4,cantidad=1)
detalle19=Detalle_Pedido(pedido=pedido10,insumo=insumo1,cantidad=1)
detalle20=Detalle_Pedido(pedido=pedido10,insumo=insumo6,cantidad=1)
detalle21=Detalle_Pedido(pedido=pedido11,insumo=insumo5,cantidad=1)
detalle22=Detalle_Pedido(pedido=pedido11,insumo=insumo8,cantidad=1)
detalle23=Detalle_Pedido(pedido=pedido12,insumo=insumo5,cantidad=4)
detalle24=Detalle_Pedido(pedido=pedido12,insumo=insumo10,cantidad=120)
detalle25=Detalle_Pedido(pedido=pedido13,insumo=insumo6,cantidad=3)
detalle26=Detalle_Pedido(pedido=pedido13,insumo=insumo10,cantidad=100)
detalle1.save()
detalle2.save()
detalle3.save()
detalle4.save()
detalle5.save()
detalle6.save()
detalle7.save()
detalle8.save()
detalle9.save()
detalle10.save()
detalle11.save()
detalle12.save()
detalle13.save()
detalle14.save()
detalle15.save()
detalle16.save()
detalle17.save()
detalle18.save()
detalle19.save()
detalle20.save()
detalle21.save()
detalle22.save()
detalle23.save()
detalle24.save()
detalle25.save()
detalle26.save()


perdida1=Perdidas(cantidad_perdida=3,fecha="2019-04-03",insumo=insumo3)
perdida2=Perdidas(cantidad_perdida=2,fecha="2019-04-03",insumo=insumo8)
perdida3=Perdidas(cantidad_perdida=5,fecha="2019-04-10",insumo=insumo8)
perdida1.save()
perdida2.save()
perdida3.save()