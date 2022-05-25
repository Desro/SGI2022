# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Almacen(models.Model):
    idcomuna = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='idcomuna')
    idalmacen = models.BigIntegerField(primary_key=True)
    nmbalmacen = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'almacen'


class Bodega(models.Model):
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen')
    idbodega = models.BigIntegerField(primary_key=True)
    capacidadmaxima = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'bodega'


class Comuna(models.Model):
    idcomuna = models.BigIntegerField(primary_key=True)
    idregion = models.ForeignKey('Region', models.DO_NOTHING, db_column='idregion')
    nmbcomuna = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'comuna'


class CuentaUsuario(models.Model):
    idcuentausuario = models.BigIntegerField(primary_key=True)
    idtipousuario = models.ForeignKey('TipoUsuario', models.DO_NOTHING, db_column='idtipousuario')
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen')
    nmbusuario = models.CharField(max_length=50)
    apellidousuario = models.CharField(max_length=100)
    email = models.CharField(max_length=320)
    password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cuenta_usuario'


class Pais(models.Model):
    idpais = models.BigIntegerField(primary_key=True)
    nmbpais = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'pais'


class Pedido(models.Model):
    idpedido = models.BigIntegerField(primary_key=True)
    idproveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='idproveedor')
    fechapedido = models.DateField()
    pedidoanulado = models.CharField(max_length=1, blank=True, null=True)
    pedidorecibido = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedido'


class PedidoLine(models.Model):
    lineid = models.BigIntegerField()
    idpedido = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='idpedido', primary_key=True)
    codigo = models.ForeignKey('Producto', models.DO_NOTHING, db_column='codigo')
    cantidad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pedido_line'
        unique_together = (('idpedido', 'lineid', 'codigo'),)


class Producto(models.Model):
    codigo = models.BigIntegerField(primary_key=True)
    idtipoproducto = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='idtipoproducto')
    idproveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='idproveedor')
    nmbproducto = models.CharField(max_length=50)
    stockminimo = models.BigIntegerField()
    stockmaximo = models.BigIntegerField()
    preciocompra = models.BigIntegerField()
    precioventa = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'producto'


class ProductoLine(models.Model):
    idbodega = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='idbodega')
    codigo = models.OneToOneField(Producto, models.DO_NOTHING, db_column='codigo', primary_key=True)
    idpedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='idpedido')
    nrolote = models.BigIntegerField()
    fechavenc = models.DateField()
    cantidad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'producto_line'
        unique_together = (('codigo', 'idpedido'),)


class Proveedor(models.Model):
    idproveedor = models.BigIntegerField(primary_key=True)
    nmbproveedor = models.CharField(max_length=50)
    email = models.CharField(max_length=320)
    fono = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Region(models.Model):
    idregion = models.BigIntegerField(primary_key=True)
    idpais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='idpais')
    nmbregion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'region'


class TipoProducto(models.Model):
    idtipoproducto = models.BigIntegerField(primary_key=True)
    nmbtipoproducto = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_producto'


class TipoUsuario(models.Model):
    idtipousuario = models.BigIntegerField(primary_key=True)
    nmbtipousuario = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'
