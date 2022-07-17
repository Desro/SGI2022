"""bodegaApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *
from .email import *
from .pdf import *
urlpatterns = [
    path('', index, name='index'),
    path('menuInicio/', menuInicio, name='menuInicio'),
    path('logout', logout, name='logout'),
    #proveedor
    path('menuProveedor/', menuProveedor, name='proveedorMenu'),
    path('proveedorNew/', proveedor_New, name='proveedorNew'),
    path('prooveedorDelete/<idproveedor>', proveedor_delete, name='proveedorDelete'),
    path('proveedorUpdate/<idproveedor>', proveedor_update, name='proveedorUpdate'),
    #producto
    path('menuProducto/', menuProducto, name='productoMenu'),
    path('productoNew/', producto_New, name='productoNew'),
    path('productoDelete/<codigo>', producto_delete, name='productoDelete'),
    path('productoUpdate/<codigo>', producto_update, name='productoUpdate'),
    #pedido
    path('menuPedido/', menuPedido, name='pedidoMenu'),
    path('pedidoNew/', pedido_New, name='pedidoNew'),
    path('pedidoDelete/<codigo>', pedido_delete, name='pedidoDelete'),
    path('pedidoUpdate/<codigo>', pedido_update, name='pedidoUpdate'),
    #bodfega
    path('menuBodega/', menuBodega, name='bodegaMenu'),
    path('bodegaNew/', bodega_New, name='bodegaNew'),
    path('bodegaDelete/<idbodega>', bodega_delete, name='bodegaDelete'),
    path('bodegaUpdate/<idbodega>', bodega_update, name='bodegaUpdate'),
    #empleado
    path('menuEmpleado/', menuEmpleado, name='empleadoMenu'),
    path('empleadoNew/', empleado_New, name='empleadoNew'),
    path('empleadoDelete/<rutusuario>', empleado_delete, name='empleadoDelete'),
    path('empleadoUpdateAdmin/<rutusuario>', empleado_updateAdmin, name='empleadoUpdateAdmin'),
    path('empleadoUpdate/<rutusuario>', empleado_update, name='empleadoUpdate'),
    #empresa
    path('menuEmpresa/', menuEmpresa, name='empresaMenu'),
    path('empresaNew/', empresa_New, name='empresaNew'),
    path('empresaDelete/<rutempresa>', empresa_delete, name='empresaDelete'),
    path('empresaUpdate/<rutempresa>', empresa_update, name='empresaUpdate'),

    path('list/', pdfCorreo, name='list'),
    path('pedidopdf/',pedidopdf,name='pedidopdf'),

    #path('pdf/',render_pdf_view,name='pdf'),
    path('cbxProductoProveedor/',pedido_producto , name='cbxProductoProveedor'),


    #recepcion
    path('recepcionMenu/', menuRecepcion, name='recepcionMenu'),
    path('recepcionNew/', recepcion_New, name='recepcionNew'),
    path('recepcionDelete/<rutempresa>', recepcion_delete, name='recepcionDelete'),
    path('recepcionUpdate/<rutempresa>', recepcion_update, name='recepcionUpdate'),

    #sucursal
    path('sucursalMenu/', menuSucursal, name='sucursalMenu'),
    path('sucursalNew/', sucursal_New, name='sucursalNew'),
    path('sucursalDelete/<idalmacen>', sucursal_delete, name='sucursalDelete'),
    path('sucursalUpdate/<idalmacen>', sucursal_update, name='sucursalUpdate'),
]
