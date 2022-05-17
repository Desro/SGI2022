import imp
from pydoc import doc
import django
from django.db import connection

def agregarProductos(marca,stockmin,stockmax,preciocompra,precioventa,tipoproducto,idproveedor):
    django_cursor=connection.cursor()
    cursor  = django_cursor.connection.cursor()
    cursor.callproc("SP_AGREGAR_PRODUCTO",[marca,stockmin,stockmax,preciocompra,precioventa,tipoproducto,idproveedor])

    
