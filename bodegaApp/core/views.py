from enum import auto
from django.shortcuts import render, redirect
from django.shortcuts import reverse
from .forms import *
from .funciones import *

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

#--------------------------------------------
def menuProducto(request):
    producto = Producto.objects.all()
    return render(request,"core/productoMenu.html",{'producto':producto})

def producto_New(request):         
    if request.method == 'POST':
        form = ProductoForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            nmbproducto = form.cleaned_data.get("nmbproducto")
            stockmin = form.cleaned_data.get("stockminimo")
            stockmax = form.cleaned_data.get("stockminimo")
            preciocompra = form.cleaned_data.get("preciocompra")
            precioventa = form.cleaned_data.get("precioventa")
            tipoproducto = form.cleaned_data.get("idtipoproducto")
            proveedor = form.cleaned_data.get("idproveedor")

            ntipoproducto= TipoProducto.objects.get(nmbtipoproducto=tipoproducto)
            nidproveedor = Proveedor.objects.get(nmbproveedor=proveedor)

            agregarProductos(nmbproducto,stockmin,stockmax,preciocompra,precioventa,ntipoproducto.idtipoproducto,nidproveedor.idproveedor)
            return redirect(reverse('productoMenu')+ "?ok")
        else:
            return redirect(reverse('productoNew')+ "?fail")
    else:
        form = ProductoForm()

    return render(request,'core/productoNew.html',{'form':form})

def producto_delete(request, codigo):
    producto = Producto.objects.get(codigo = codigo)
    producto.delete()
    return redirect(to="productoMenu")

def producto_update(request, codigo):
    producto = Producto.objects.get(codigo = codigo)
    form = ProductoForm(instance = producto)

    if request.method == 'POST':
        form = ProductoForm(request.POST,request.FILES,instance=producto)
        if form.is_valid():
            form.save()                
            return redirect(reverse('productoMenu')+ "?ok")
        else:
            return redirect(reverse('productoUpdate')+ codigo)

    return render(request,'core/productoUpdate.html',{'form':form})

#----------------------------------
def menuPedido(request):
    pedido = Pedido.objects.all()
    return render(request,"core/pedidoMenu.html",{'pedido':pedido})

def pedido_New(request):         
    if request.method == 'POST':
        form = PedidoFormP(request.POST or None,request.FILES or None)
        if form.is_valid():
            idproveedor = form.cleaned_data.get("idproveedor")
            proveedorElegido = Proveedor.objects.get(nmbproveedor=idproveedor)
            return render(request,'core/pedidoNew.html',{'proveedorElegido':proveedorElegido}) 
        else:
            return redirect(reverse('pedidoNew')+ "?fail")
    else:
        form = PedidoFormP()
    return render(request,'core/pedidoNew.html',{'form':form})

def pedido_New1(request,proveedorE):
    proveedorElegido= Proveedor.objects.get(nmproveedor= proveedorE)
    return render(request,'core/pedidoNew.html',{'proveedorElegido':proveedorElegido})

def pedido_delete(request, codigo):
    producto = Producto.objects.get(codigo = codigo)
    producto.delete()
    return redirect(to="productoMenu")

def pedido_update(request, codigo):
    producto = Producto.objects.get(codigo = codigo)
    form = ProductoForm(instance = producto)

    if request.method == 'POST':
        form = ProductoForm(request.POST,request.FILES,instance=producto)
        if form.is_valid():
            form.save()                
            return redirect(reverse('productoMenu')+ "?ok")
        else:
            return redirect(reverse('productoUpdate')+ codigo)

    return render(request,'core/productoUpdate.html',{'form':form})
