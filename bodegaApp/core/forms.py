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
