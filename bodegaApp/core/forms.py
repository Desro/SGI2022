from dataclasses import field
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import *
class ProveedorForm(forms.ModelForm):
    
    class Meta:
        model = Proveedor

        fields = [
            'idproveedor',
            'nmbproveedor',
            'email',
            'fono'
        ]        
        
        labels = {
            'idproveedor':'id Proveedro',
            'nmbproveedor':'Nombre Proveedor',
            'email':'Email',
            'fono':'Telefono'
        }
        widgets = {
            'idproveedor':forms.TextInput(attrs={'class':'form-control'}),
            'nmbproveedor':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'email':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'fono':forms.TextInput(attrs={'class':'form-control','type':'text'}),

        }

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto

        fields = [
            'nmbproducto',
            'stockminimo',
            'stockmaximo',
            'preciocompra',
            'precioventa',
            'idtipoproducto',
            'idproveedor',

        ]        
        
        labels = {
            'nmbproducto':'Nombre Producto',
            'stockminimo':'Stock Minimo',
            'stockmaximo':'Stock Maximo',
            'preciocompra':'Precio Compra',
            'precioventa':'Precio Venta',
            'idtipoproducto':'Tipo Producto',
            'idproveedor':'Proveedor',
           
        }
        widgets = {
            'nmbproducto':forms.TextInput(attrs={'class':'form-control'}),
            'stockminimo':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'stockmaximo':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'preciocompra':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'precioventa':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'idtipoproducto':forms.Select(attrs={'class':'form-control'}),
            'idproveedor':forms.Select(attrs={'class':'form-control'}),

        }

class PedidoFormP(forms.ModelForm):
    
    class Meta:
        model = Pedido

        fields = [
            'idproveedor'
            
        ]        
        
        labels = {
            'idproveedor':'Proveedor'
            

           
        }
        widgets = {
            'idproveedor':forms.Select(attrs={'class':'form-control'}),
            
        }