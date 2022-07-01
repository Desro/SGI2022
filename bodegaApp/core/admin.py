from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(TipoProducto)
admin.site.register(TipoUsuario)
admin.site.register(Producto)
admin.site.register(ProductoLine)
admin.site.register(Pedido)
admin.site.register(PedidoLine)
admin.site.register(Almacen)
admin.site.register(Provincia)
admin.site.register(Region)
admin.site.register(CuentaUsuario)
admin.site.register(Bodega)
admin.site.register(Comuna)
admin.site.register(Proveedor)
admin.site.register(Empresa)