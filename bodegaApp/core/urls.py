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

urlpatterns = [
    path('', index, name='index'),
    path('registroUsuario/', registroUsuario, name='registroUsuario'),
    path('menuProveedor/', menuProveedor, name='proveedorMenu'),
    path('proveedorNew/', proveedor_New, name='proveedorNew'),
    path('prooveedorDelete/<idproveedor>', proveedor_delete, name='proveedorDelete'),
    path('proveedorUpdate/<idproveedor>', proveedor_update, name='proveedorUpdate'),
    path('menuProducto/', menuProducto, name='productoMenu'),
    path('productoNew/', producto_New, name='productoNew'),
    path('productoDelete/<codigo>', producto_delete, name='productoDelete'),
    path('productoUpdate/<codigo>', producto_update, name='productoUpdate'),
    path('menuPedido/', menuPedido, name='pedidoMenu'),
    path('pedidoNew/', pedido_New, name='pedidoNew'),
    path('pedidoDelete/<codigo>', pedido_delete, name='pedidoDelete'),
    path('pedidoUpdate/<codigo>', pedido_update, name='pedidoUpdate'),
]
