import imp
from pydoc import doc
import django
from django.db import connection

def agregarProductos(nmbproducto,stockmin,stockmax,preciocompra,precioventa,tipoproducto,idproveedor):
    django_cursor=connection.cursor()
    cursor  = django_cursor.connection.cursor()
    cursor.callproc("SP_AGREGAR_PRODUCTO",[nmbproducto,stockmin,stockmax,preciocompra,precioventa,tipoproducto,idproveedor])

def crearPedido(opcion,idpedido,cantidad,producto):
    django_cursor=connection.cursor()
    cursor  = django_cursor.connection.cursor()
    cursor.callproc("SP_CREAR_PEDIDO",[opcion,idpedido,cantidad,producto])

    
