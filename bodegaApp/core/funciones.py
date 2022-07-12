import imp
from pydoc import doc
import django
from django.db import connection

def agregarProductos(nmbproducto,stockmin,stockmax,preciocompra,precioventa,tipoproducto,idproveedor):
    django_cursor=connection.cursor()
    cursor  = django_cursor.connection.cursor()
    cursor.callproc("SP_AGREGAR_PRODUCTO",[nmbproducto,stockmin,stockmax,preciocompra,precioventa,tipoproducto,idproveedor])
    cursor.close()

def crearPedido(opcion,idpedido,cantidad,producto):
    django_cursor=connection.cursor()
    cursor  = django_cursor.connection.cursor()
    cursor.callproc("SP_CREAR_PEDIDO",[opcion,idpedido,cantidad,producto])
    cursor.close()
    
def crearUsuario(idusuario,idtipousuario,idalmacen,nmbusuario,apellido,email):
    django_cursor=connection.cursor()
    cursor  = django_cursor.connection.cursor()
    cursor.callproc("SP_CREAR_USUARIO",[idusuario,idtipousuario,idalmacen,nmbusuario,apellido,email])
    cursor.close()

def estadoBodega():
    django_cursor=connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur=django_cursor.connection.cursor()

    cursor.callproc("SP_ESTADO_BODEGA",[out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)

    return lista

def estadoProducto():
    django_cursor=connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur=django_cursor.connection.cursor()

    cursor.callproc("SP_ESTADO_PRODUCTO",[out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)

    return lista

#######OSCAR
def agregarPedido(idproveedor):
    idprov=str(idproveedor)
    django_cursor=connection.cursor()
    cursor  = django_cursor.connection.cursor()
    query ="insert into pedido (idpedido,idproveedor,fechapedido,pedidoanulado,pedidorecibido) values (12,"+idprov+",SYSDATE,'1','1')"
    cursor.execute(query)
    #cursor.execute("insert into pedido (idpedido,idproveedor,fechapedido,pedidoanulado,pedidorecibido) values (12, %s,SYSDATE,'1','1')", [idprov])
    
