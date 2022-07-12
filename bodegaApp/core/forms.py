from dataclasses import field, fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .model import *

class ProveedorForm(forms.ModelForm):
    
    class Meta:
        model = Proveedor

        fields = [
            'nmbproveedor',
            'rutempresa',
            'email',
            'fono',
            'personadecontacto'

        ]        
        
        labels = {
            'nmbproveedor':'Nombre Proveedor',
            'email':'Email',
            'rutempresa':'Empresa',
            'fono':'Telefono',
            'personadecontacto':'Persona de Contacto',
        }
        widgets = {
            'nmbproveedor':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'email':forms.EmailInput(attrs={'class':'form-control','type':'email'}),
            'fono':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'rutempresa':forms.Select(attrs={'class':'form-control'}),
            'personadecontacto':forms.TextInput(attrs={'class':'form-control','type':'text'}),
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
<<<<<<< Updated upstream
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
=======
            'idproveedor':'Proveedor',
            
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
            'rutusuario':forms.TextInput(attrs={'class':'form-control'}),
            'nmbusuario':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'apellidousuario':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'password':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'email':forms.EmailInput(attrs={'class':'form-control','type':'email'}),
            'idalmacen':forms.Select(attrs={'class':'form-control'}),
=======
            'idproveedor':forms.TextInput(attrs={'class':'form-control'}),
>>>>>>> Stashed changes
            

        }

<<<<<<< Updated upstream
class EmpresaForm(forms.ModelForm):
=======


class BodegaForm(forms.ModelForm):
>>>>>>> Stashed changes
    
    class Meta:
        model = Empresa

        fields = [
            'rutempresa',
            'nmbempresa',
            'direccion',
            'idcomuna',

        ]        
        
        labels = {
            'rutempresa':'Rut Empresa:',
            'nmbempresa':'Nombre Empresa : ',
            'direccion':'Direccion :',
            'idcomuna':'Comuna :',
            'password':'Contraseña :',
            'idalmacen':'Almacen :',
           
        }
        widgets = {
<<<<<<< Updated upstream
            'rutempresa':forms.TextInput(attrs={'class':'form-control'}),
            'nmbempresa':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'direccion':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'idcomuna':forms.Select(attrs={'class':'form-control'}),
            

=======
            'idalmacen':forms.Select(attrs={'class':'form-control'}),
            'capacidadmaxima':forms.TextInput(attrs={'class':'form-control','type':'text'}),
>>>>>>> Stashed changes
        }



<<<<<<< Updated upstream
=======
class PedidoNuevoForm(forms.ModelForm):
    
    class Meta:
        model = Pedido

        fields = [
            'idproveedor'
            
        ]        
        
        labels = {
            'idproveedor':'Proveedor',
            

           
        }
        widgets = {
            'idproveedor':forms.TextInput(attrs={'class':'form-control'}),
            
        }
>>>>>>> Stashed changes
