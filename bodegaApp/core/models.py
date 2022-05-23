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
    def _str_(self):
        return self.nmbcomuna


class CuentaUsuario(models.Model):
    idcuentausuario = models.BigIntegerField(primary_key=True)
    nmbusuario = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=320)
    password = models.CharField(max_length=50)
    idtipousuario = models.ForeignKey('TipoUsuario', models.DO_NOTHING, db_column='idtipousuario')
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen')

    class Meta:
        managed = False
        db_table = 'cuenta_usuario'


class Pais(models.Model):
    idpais = models.BigIntegerField(primary_key=True)
    nmbpais = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'pais'

    def _str_(self):
        return self.nmbpais

class Pedido(models.Model):
    idpedido = models.BigIntegerField(primary_key=True)
    fechapedido = models.DateField()
    pedidoanulado = models.CharField(max_length=1)
    pedidorecibido = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'pedido'


class PedidoLine(models.Model):
    idpedido = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='idpedido', primary_key=True)
    codigo = models.ForeignKey('Producto', models.DO_NOTHING, db_column='codigo')
    cantidad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pedido_line'


class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=100)
    marca = models.CharField(max_length=50)
    stockminimo = models.BigIntegerField()
    stockmaximo = models.BigIntegerField()
    preciocompra = models.BigIntegerField()
    precioventa = models.BigIntegerField()
    idtipoproducto = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='idtipoproducto')
    idproveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='idproveedor')

    class Meta:
        managed = False
        db_table = 'producto'
    def _str_(self):
        return self.marca


class ProductoLine(models.Model):
    idpedido = models.ForeignKey(PedidoLine, models.DO_NOTHING, db_column='idpedido')
    producto_codigo = models.ForeignKey(Producto, models.DO_NOTHING, db_column='producto_codigo')
    nrolote = models.BigIntegerField()
    fechavenc = models.DateField()
    cantidad = models.BigIntegerField()
    bodega_idbodega = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='bodega_idbodega')

    class Meta:
        managed = False
        db_table = 'producto_line'


class Proveedor(models.Model):
    idproveedor = models.BigIntegerField(primary_key=True)
    nmbproveedor = models.CharField(max_length=50)
    email = models.CharField(max_length=320)
    fono = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'proveedor'
    def _str_(self):
        return self.nmbproveedor


class Region(models.Model):
    idregion = models.BigIntegerField(primary_key=True)
    idpais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='idpais')
    nmbregion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'region'
    def _str_(self):
        return self.nmbregion


class TipoProducto(models.Model):
    idtipoproducto = models.BigIntegerField(primary_key=True)
    nmbtipoproducto = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_producto'

    def _str_(self):
        return self.nmbtipoproducto

class TipoUsuario(models.Model):
    idtipousuario = models.BigIntegerField(primary_key=True)
    nmbtipousuario = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'
    def _str_(self):
        return self.nmbtipousuario