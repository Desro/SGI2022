from dataclasses import field
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import *

class ProveedorForm(forms.ModelForm):
    
    class Meta:
        model = Proveedor

        fields = [
            'nmbproveedor',
            'email',
            'fono'
        ]        
        
        labels = {
            'nmbproveedor':'Nombre Proveedor',
            'email':'Email',
            'fono':'Telefono'
        }
        widgets = {
            'nmbproveedor':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'email':forms.EmailInput(attrs={'class':'form-control','type':'email'}),
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


class BodegaForm(forms.ModelForm):
    
    class Meta:
        model = Bodega

        fields = [
            'idalmacen',
            'capacidadmaxima'
        ]        
        
        labels = {
            'idalmacen':'Almacen',
            'capacidadmaxima':'Capacidad Maxima',
        }
        widgets = {
            'idalmacen':forms.Select(attrs={'class':'form-control'}),
            'capacidadmaxima':forms.TextInput(attrs={'class':'form-control','type':'text'}),
        }

class EmpleadosForm(forms.ModelForm):
    
    class Meta:
        model = CuentaUsuario

        fields = [
            'rutusuario',
            'nmbusuario',
            'idalmacen',
            'apellidousuario',
            'email',
            'password',

        ]        
        
        labels = {
            'rutusuario':'Rut',
            'nmbusuario':'Nombre : ',
            'apellidousuario':'Apellido :',
            'email':'Email :',
            'password':'Contraseña :',
            'idalmacen':'Almacen :',
           
        }
        widgets = {
            'rutusuario':forms.TextInput(attrs={'class':'form-control'}),
            'nmbusuario':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'apellidousuario':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'password':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'email':forms.EmailInput(attrs={'class':'form-control','type':'email'}),
            'idalmacen':forms.Select(attrs={'class':'form-control'}),
            

        }


