# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Almacen(models.Model):
    idalmacen = models.BigIntegerField(primary_key=True)
    idcomuna = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='idcomuna')
    nmbalmacen = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'almacen'
    
    def __str__(self):
        return self.nmbalmacen


class Bodega(models.Model):
    idbodega = models.BigIntegerField(primary_key=True)
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen')
    capacidadmaxima = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'bodega'
    
    def __str__(self):
        return self.idalmacen


class Comuna(models.Model):
    idcomuna = models.BigIntegerField(primary_key=True)
    idprovincia = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='idprovincia')
    descripcion = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'comuna'

    def __str__(self):
        return self.descripcion

class CuentaUsuario(models.Model):
    idcuentausuario = models.BigIntegerField(primary_key=True)
    idtipousuario = models.ForeignKey('TipoUsuario', models.DO_NOTHING, db_column='idtipousuario')
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen')
    nmbusuario = models.CharField(max_length=50)
    apellidousuario = models.CharField(max_length=100)
    email = models.CharField(max_length=320)
    password = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta_usuario'


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
    idpedido = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='idpedido', primary_key=True)
    codigo = models.ForeignKey('Producto', models.DO_NOTHING, db_column='codigo')
    lineid = models.BigIntegerField()
    cantidad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pedido_line'
        unique_together = (('idpedido', 'lineid', 'codigo'),)


class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=100)
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
    
    def __str__(self):
        return self.nmbproducto


class ProductoLine(models.Model):
    idpedido = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='idpedido', primary_key=True)
    codigo = models.ForeignKey(Producto, models.DO_NOTHING, db_column='codigo')
    idbodega = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='idbodega')
    nrolote = models.BigIntegerField()
    fechavenc = models.DateField()
    cantidad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'producto_line'
        unique_together = (('idpedido', 'codigo'),)


class Proveedor(models.Model):
    idproveedor = models.BigIntegerField(primary_key=True)
    nmbproveedor = models.CharField(max_length=50)
    email = models.CharField(max_length=320)
    fono = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'proveedor'
    
    def __str__(self):
        return self.nmbproveedor


class Provincia(models.Model):
    idprovincia = models.BigIntegerField(primary_key=True)
    idregion = models.ForeignKey('Region', models.DO_NOTHING, db_column='idregion')
    descripcion = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'provincia'


class Region(models.Model):
    idregion = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=60)

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
