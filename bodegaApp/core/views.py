from asyncio.windows_events import NULL
from enum import auto
from operator import ge
from traceback import print_tb
from webbrowser import get
from django.shortcuts import render, redirect
from django.shortcuts import reverse
from .forms import *
from .funciones import *
from .email import *


# Create your views here.
def index(request):
    return render(request,"core/index.html")


#------PROVEEDOR
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
    #form = PedidoFormP()
    #if request.method == 'POST':
    #    form = PedidoFormP(request.POST,request.FILES)
    #    if form.is_valid():
    #        idproveedor = form.cleaned_data.get("idproveedor")
     #       proveedorElegido= Proveedor.objects.get(nmbproveedor= idproveedor)
     #       productos=Producto.objects.get(idproveedor=proveedorElegido.idproveedo)
     #       return render(request,'core/pedidoNew.html',{'proveedorElegido':proveedorElegido},{'productos':productos})

    return render(request,'core/pedidoNew.html')


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

#------USUARIO---------------------
def menuEmpleado(request):
    cuentaUsuario = CuentaUsuario.objects.all()
    return render(request,"core/empleadoMenu.html",{'cuentaUsuario':cuentaUsuario})

def empleado_New(request):         
    if request.method == 'POST':
        form = EmpleadosForm(request.POST or None,request.FILES or None)
        if form.is_valid():        
            idcuentausuario =form.cleaned_data.get("idcuentausuario")
            apellidousuario = form.cleaned_data.get("apellidousuario")
            nmbusuario = form.cleaned_data.get("nmbusuario")
            email = form.cleaned_data.get("email")
            idalmacen=form.cleaned_data.get("idalmacen")
            
            idcuentausuario =form.cleaned_data.get("idcuentausuario")
            apellidousuario = form.cleaned_data.get("apellidousuario")
            nmbusuario = form.cleaned_data.get("nmbusuario")
            email = form.cleaned_data.get("email")
            idalmacen=form.cleaned_data.get("idalmacen")
            
            nidalmacen = Almacen.objects.get(nmbalmacen=idalmacen)
            print(nidalmacen)
            crearUsuario(idcuentausuario,2,nidalmacen.idalmacen,nmbusuario,apellidousuario,email)
            send_emailNewEmpleado(email,idcuentausuario)   
   
            return redirect(reverse('empleadoMenu')+ "?ok")
        else:
            return redirect(reverse('empleadoNew')+ "?fail")
    else:
        form = EmpleadosForm()

    return render(request,'core/empleadoNew.html',{'form':form})

def empleado_delete(request, idcuentausuario):
    cuentaUsuario = CuentaUsuario.objects.get(idcuentausuario = idcuentausuario)
    try:
        cuentaUsuario.delete()
        return redirect(to="empleadoMenu")
    except:
       return redirect(reverse('empleadoMenu')+ "?errorPK")
       

def empleado_updateAdmin(request, idcuentausuario):
    cuentaUsuario = CuentaUsuario.objects.get(idcuentausuario = idcuentausuario)
    form = EmpleadosForm(instance = cuentaUsuario)

    if request.method == 'POST':
        form = EmpleadosForm(request.POST,request.FILES,instance=cuentaUsuario)
        if form.is_valid():
            form.save()                
            return redirect(reverse('empleadoMenu')+ "?ok")
        else:
            return redirect(reverse('empleadoUpdateAdmin')+ idcuentausuario)

    return render(request,'core/empleadoUpdateAdmin.html',{'form':form})

def empleado_update(request, idproveedor):
    proveedor = Proveedor.objects.get(idproveedor = idproveedor)
    form = ProveedorForm(instance = proveedor)

    if request.method == 'POST':
        form = ProveedorForm(request.POST,request.FILES,instance=proveedor)
        if form.is_valid():
            form.save()                
            return redirect(reverse('empleadoMenu')+ "?ok")
        else:
            return redirect(reverse('proveedorUpdate')+ idproveedor)

    return render(request,'core/proveedorUpdate.html',{'form':form})


def menuInicio(request):
    listaProductoMax = []
    listaProductoMin = []
    listaBodega=[]

    for fila in estadoBodega():
        if fila[1]  >= Bodega.objects.get(idbodega=fila[0]).capacidadmaxima -100:
            listaBodega.append(fila)

    for fila in estadoProducto():
        if fila[1]  >= Producto.objects.get(codigo=fila[0]).stockmaximo -100:
            listaProductoMax.append(fila)
        if fila[1]  <= Producto.objects.get(codigo=fila[0]).stockminimo +100:
            listaProductoMin.append(fila)
    data = {
        'estadoBodega':listaBodega,
        'stockMax':listaProductoMax,
        'stockMin':listaProductoMin
    } 
    return render(request,'core/menuInicio.html',data)



