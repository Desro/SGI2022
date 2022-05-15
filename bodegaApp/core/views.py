from enum import auto
from django.shortcuts import render, redirect
from django.shortcuts import reverse
from .forms import *
# Create your views here.
def index(request):

    return render(request,"core/index.html")

def registroUsuario(request):
    return render(request,"core/registroUsuario.html")

def menuProveedor(request):
    proveedor = Proveedor.objects.all()
    return render(request,"core/proveedorMenu.html",{'proveedor':proveedor})

def proveedor_New(request):         
    if request.method == 'POST':
        form = ProveedorForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            idproveedor = form.cleaned_data.get("idproveedor")
            nmbproveedor = form.cleaned_data.get("nmbproveedor")
            email = form.cleaned_data.get("email")
            fono = form.cleaned_data.get("fono")
            obj = Proveedor.objects.create(
                idproveedor=idproveedor,
                nmbproveedor=nmbproveedor,
                email=email,
                fono=fono,
            )
            obj.save()            
            return redirect(reverse('proveedorMenu')+ "?ok")
        else:
            return redirect(reverse('proveedorNew')+ "?fail")
    else:
        form = ProveedorForm()

    return render(request,'core/proveedorNew.html',{'form':form})

def proveedor_delete(request, idproveedor):
    proveedor = Proveedor.objects.get(idproveedor = idproveedor)
    proveedor.delete()
    return redirect(to="proveedorMenu")

def proveedor_update(request, idproveedor):
    proveedor = Proveedor.objects.get(idproveedor = idproveedor)
    form = ProveedorForm(instance = proveedor)

    if request.method == 'POST':
        form = ProveedorForm(request.POST,request.FILES,instance=proveedor)
        if form.is_valid():
            form.save()                
            return redirect(reverse('proveedorMenu')+ "?ok")
        else:
            return redirect(reverse('proveedorUpdate')+ idproveedor)

    return render(request,'core/proveedorUpdate.html',{'form':form})
