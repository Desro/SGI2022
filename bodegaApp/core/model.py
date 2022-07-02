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
    direccion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'almacen'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bodega(models.Model):
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen')
    idbodega = models.BigIntegerField(primary_key=True)
    capacidadmaxima = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'bodega'


class Comuna(models.Model):
    idcomuna = models.BigIntegerField(primary_key=True)
    idprovincia = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='idprovincia')
    descripcion = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'comuna'


class CuentaUsuario(models.Model):
    rutusuario = models.CharField(primary_key=True, max_length=11)
    idtipousuario = models.ForeignKey('TipoUsuario', models.DO_NOTHING, db_column='idtipousuario')
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen')
    nmbusuario = models.CharField(max_length=50)
    apellidousuario = models.CharField(max_length=100)
    email = models.CharField(max_length=320)
    password = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta_usuario'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresa(models.Model):
    rutempresa = models.CharField(primary_key=True, max_length=11)
    nmbempresa = models.CharField(max_length=50)
    idcomuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='idcomuna')
    direccion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'empresa'


class Pedido(models.Model):
    idpedido = models.BigIntegerField(primary_key=True)
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


class ProductoLine(models.Model):
    nrolote = models.BigIntegerField(primary_key=True)
    codigo = models.ForeignKey(Producto, models.DO_NOTHING, db_column='codigo')
    idbodega = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='idbodega')
    idpedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='idpedido')
    fechavenc = models.DateField()
    cantidad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'producto_line'


class Proveedor(models.Model):
    idproveedor = models.BigIntegerField(primary_key=True)
    rutempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='rutempresa')
    nmbproveedor = models.CharField(max_length=50)
    email = models.CharField(max_length=320)
    fono = models.CharField(max_length=50)
    personadecontacto = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'


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
