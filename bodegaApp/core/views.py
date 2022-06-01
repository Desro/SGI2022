from asyncio.windows_events import NULL
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
            idproveedor = Proveedor.objects.count()+1                      
            try:
                pp = Proveedor.objects.get(idproveedor=idproveedor).idproveedor
                while pp != NULL:
                    idbodega= idbodega+10
                    pp = Proveedor.objects.get(idproveedor=idproveedor).idproveedor
            except:
                idproveedor=idproveedor

            idbodega = Bodega.objects.count()+1
           
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
    try:
        proveedor.delete()
        return redirect(to="proveedorMenu")
    except:
       return redirect(reverse('proveedorMenu')+ "?errorPK")
       

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
    form = PedidoFormP()
    if request.method == 'POST':
        form = PedidoFormP(request.POST,request.FILES)
        if form.is_valid():
            idproveedor = form.cleaned_data.get("idproveedor")
            proveedorElegido= Proveedor.objects.get(nmbproveedor= idproveedor)
            productos=Producto.objects.get(idproveedor=proveedorElegido.idproveedo)
            return render(request,'core/pedidoNew.html',{'proveedorElegido':proveedorElegido},{'productos':productos})

    return render(request,'core/pedidoNew.html',{'form':form})


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
#--------------------------------------------
def menuBodega(request):
    bodega = Bodega.objects.all()
    return render(request,"core/bodegaMenu.html",{'bodega':bodega})

def bodega_New(request):         
    if request.method == 'POST':
        form = BodegaForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            idbodega = Bodega.objects.count()+1
            try:
                bb = Bodega.objects.get(idbodega=idbodega).idbodega
                while bb != NULL:
                    idbodega= idbodega+10
                    bb = Bodega.objects.get(idbodega=idbodega).idbodega
            except:
                idbodega=idbodega
            idalmacen = form.cleaned_data.get("idalmacen")
            capacidadmaxima = form.cleaned_data.get("capacidadmaxima")            
            obj = Bodega.objects.create(
                idbodega=idbodega,
                idalmacen=idalmacen,
                capacidadmaxima=capacidadmaxima,
            )

            obj.save()           
            return redirect(reverse('bodegaMenu')+ "?ok")
        else:
            return redirect(reverse('bodegaNew')+ "?fail")
       
    else:
        form = BodegaForm()

    return render(request,'core/bodegaNew.html',{'form':form})

def bodega_delete(request, idbodega):
    producto = Bodega.objects.get(idbodega = idbodega)
    try:
        producto.delete()
        return redirect(to="bodegaMenu")
    except:
        return redirect(reverse('bodegaMenu')+ "?errorPK")
    

def bodega_update(request, idbodega):
    bodega = Bodega.objects.get(idbodega = idbodega)
    form = BodegaForm(instance = bodega)

    if request.method == 'POST':
        form = BodegaForm(request.POST,request.FILES,instance=bodega)
        if form.is_valid():
            form.save()                
            return redirect(reverse('bodegaMenu')+ "?ok")
        else:
            return redirect(reverse('bodegaUpdate')+ idbodega)

    return render(request,'core/bodegaUpdate.html',{'form':form})

#----------------------------------