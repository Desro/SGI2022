from asyncio.windows_events import NULL
from dataclasses import dataclass
from distutils.command.clean import clean
import email
from enum import auto
from itertools import product
from math import prod
from multiprocessing import context
from operator import ge
from pickle import TRUE
from traceback import print_tb
from urllib import response
from webbrowser import get
from django.shortcuts import render, redirect
from django.shortcuts import reverse
from django.views import View
from .forms import *
from .funciones import *
from .email import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .model import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .pdf import *
# Create your views here.


##----------
from distutils import core
import imp
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

def index(request):
    if request.method == 'GET':
        return render(request,"core/index.html")
        
    if request.method == 'POST':
        email = request.POST.get("email")
        password=  request.POST.get("password")        
        emailbd= CuentaUsuario.objects.filter(email=(email)).count()
        print(emailbd)
        if (emailbd) > 0:
            if password == CuentaUsuario.objects.get(email=email).password :
                request.session['email']=email
                tipoUsuario= CuentaUsuario.objects.get(email=email).idtipousuario
                store =  CuentaUsuario.objects.get(email=email).idalmacen
                tipousuarionro=TipoUsuario.objects.get(nmbtipousuario=tipoUsuario).idtipousuario
                storenro=Almacen.objects.get(nmbalmacen=store).idalmacen
                nmbusuario =CuentaUsuario.objects.get(email=email).nmbusuario
                apellidousuario=CuentaUsuario.objects.get(email=email).apellidousuario

                request.session['tipo_usuario']=[tipousuarionro]
                request.session['login_status']=[True]
                request.session['store']=[storenro]
                request.session['nmbusuario']=[nmbusuario]
                request.session['apellidousuario']=[apellidousuario]
                
                response= redirect(reverse('menuInicio'))
                response.set_cookie('tipo_usuario',tipousuarionro)
                response.set_cookie('login_status',True)
                response.set_cookie('store',storenro)
                response.set_cookie('nmbusuario',nmbusuario)
                response.set_cookie('apellidousuario',apellidousuario)


                return response
                #return redirect(reverse('menuInicio'),{'tipoUsuario':tipoUsuario})
            else:
              
                return redirect(reverse('index')+ "?fail1")
                
        else:

            return redirect(reverse('index')+ "?fail2")

    return render(request,"core/index.html")

#---------------

def menuInicio(request):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:        
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

        page= request.GET.get('page',1)


        paginatorProducMax= Paginator(listaProductoMax,3)
        paginatorProducMin= Paginator(listaProductoMin,3)
        paginatorBodega= Paginator(listaBodega,3)
        
        #PAGINACION PRODUCTOS MAXIMOS
        try:
            listaProductoMax=paginatorProducMax.page(page)
        except PageNotAnInteger:
            listaProductoMax=paginatorProducMax.page(1)
        except EmptyPage:
            listaProductoMax=paginatorProducMax.page(paginatorProducMax.num_pages)

        #PAGINACION PRODUCTO MINIMO
        try:
            listaProductoMin=paginatorProducMin.page(page)
        except PageNotAnInteger:
            listaProductoMax=paginatorProducMin.page(1)
        except EmptyPage:
            listaProductoMax=paginatorProducMin.page(paginatorProducMin.num_pages)

        #PAGINACION BODEGA
        try:
            listaBodega=paginatorBodega.page(page)
        except PageNotAnInteger:
            listaBodega=paginatorBodega.page(1)
        except EmptyPage:
            listaBodega=paginatorBodega.page(paginatorBodega.num_pages)



        data = {
            'estadoBodega':listaBodega,
            'stockMax':listaProductoMax,
            'stockMin':listaProductoMin,
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        } 
    else:
            data = {
            'tipo_usuario': 6666,
            'login_status': False,
        }  
    return render(request,'core/menuInicio.html',data)

#----LOGOUT
def logout(request):
    response = HttpResponseRedirect(reverse('index'))

    response.delete_cookie('tipo_usuario')
    response.set_cookie('login_status',False)
    response.delete_cookie('store')
    response.delete_cookie('nmbusuario')
    response.delete_cookie('apellidousuario')
    
    return response
#------PROVEEDOR
def menuProveedor(request):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        proveedor = Proveedor.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(proveedor,5)

        try :
            proveedor = paginator.page(page)
        except PageNotAnInteger :
            proveedor = paginator.page(1)
        except EmptyPage:
            proveedor = paginator.page(proveedor.num_pages)
        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'proveedor':proveedor,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        }
    else:
        data = {
        'tipo_usuario': 6666,
        'login_status': False,
    }  
    return render(request,"core/proveedorMenu.html",data)

def proveedor_New(request):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        if request.method == 'POST':
            form = ProveedorForm(request.POST or None,request.FILES or None)
            if form.is_valid():
                idproveedor = Proveedor.objects.count()+1                      
                try:
                    pp = Proveedor.objects.get(idproveedor=idproveedor).idproveedor
                    while pp != NULL:
                        idproveedor= idproveedor+10
                        pp = Proveedor.objects.get(idproveedor=idproveedor).idproveedor
                except:
                    idproveedor=idproveedor

                nmbempresa = form.cleaned_data.get("rutempresa")
                rutempresa=Empresa.objects.get(nmbempresa=nmbempresa)
                nmbproveedor = form.cleaned_data.get("nmbproveedor")
                email = form.cleaned_data.get("email")
                fono = form.cleaned_data.get("fono")
                personadecontacto=form.cleaned_data.get("personadecontacto")
                obj = Proveedor.objects.create(
                    rutempresa= rutempresa,
                    idproveedor=idproveedor,
                    nmbproveedor=nmbproveedor,
                    email=email,
                    fono=fono,
                    personadecontacto=personadecontacto,
                )

                obj.save()            
                return redirect(reverse('proveedorMenu')+ "?ok")
            else:
                return redirect(reverse('proveedorNew')+ "?fail")
        else:
            form = ProveedorForm()
        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'form':form,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        }  
    else:
        data = {
        'tipo_usuario': 6666,
        'login_status': False,
    }          
   

    return render(request,'core/proveedorNew.html',data)

def proveedor_delete(request, idproveedor):
    proveedor = Proveedor.objects.get(idproveedor = idproveedor)
    try:
        proveedor.delete()
        return redirect(to="proveedorMenu")
    except:
       return redirect(reverse('proveedorMenu')+ "?errorPK")
       

def proveedor_update(request, idproveedor):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        proveedor = Proveedor.objects.get(idproveedor = idproveedor)
        form = ProveedorForm(instance = proveedor)

        if request.method == 'POST':
            form = ProveedorForm(request.POST,request.FILES,instance=proveedor)
            if form.is_valid():
                form.save()                
                return redirect(reverse('proveedorMenu')+ "?ok")
            else:
                return redirect(reverse('proveedorUpdate')+ idproveedor)
            
        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'form':form,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        }
    else:
        data = {
        'tipo_usuario': 6666,
        'login_status': False,
    } 
    
    return render(request,'core/proveedorUpdate.html',data)

#--------PRODUCTO------------------------
def menuProducto(request):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        producto = Producto.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(producto,5)

        try :
            producto = paginator.page(page)
        except PageNotAnInteger :
            producto = paginator.page(1)
        except EmptyPage:
            producto = paginator.page(producto.num_pages)
        
        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'producto':producto,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        }    
    else:
        data = {
        'tipo_usuario': 6666,
        'login_status': False,
    }     
    return render(request,"core/productoMenu.html",data)

def producto_New(request):

    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
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
        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'form':form,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        }    
    else:
        data = {
        'tipo_usuario': 6666,
        'login_status': False,
    }  

    

    return render(request,'core/productoNew.html',data)

def producto_delete(request, codigo):
    producto = Producto.objects.get(codigo = codigo)
    producto.delete()
    return redirect(to="productoMenu")

def producto_update(request, codigo):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        producto = Producto.objects.get(codigo = codigo)
        form = ProductoForm(instance = producto)

        if request.method == 'POST':
            form = ProductoForm(request.POST,request.FILES,instance=producto)
            if form.is_valid():
                form.save()                
                return redirect(reverse('productoMenu')+ "?ok")
            else:
                return redirect(reverse('productoUpdate')+ codigo)        
        data ={
                'tipo_usuario': request.COOKIES['tipo_usuario'],
                'login_status': request.COOKIES['login_status'],
                'store': request.COOKIES['store'],
                'form':form,
                'nmbusuario': request.COOKIES['nmbusuario'],
                'apellidousuario': request.COOKIES['apellidousuario'],
            }    
    else:
        data = {
        'tipo_usuario': 6666,
        'login_status': False,
    } 
    

    return render(request,'core/productoUpdate.html',data)

#------PEDIDO------------------
def menuPedido(request):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        pedido = Pedido.objects.all()

        page = request.GET.get('page',1)
        paginator = Paginator(pedido,5)

        try :
            pedido = paginator.page(page)
        except PageNotAnInteger :
            pedido = paginator.page(1)
        except EmptyPage:
            pedido = paginator.page(pedido.num_pages)
        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'pedido':pedido,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        }  
    else:
        data = {
        'tipo_usuario': 6666,
        'login_status': False,
    }  
    return render(request,"core/pedidoMenu.html",data)
####OSCAR
def pedido_New(request): 
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:        
        proveedor = Proveedor.objects.all()
        print(proveedor)
        print("llega")
        if request.method == 'POST':
            form = request.POST.get("idproveedor")
            proveedor = request.POST.get("idproveedor")
            print ("proveedor")
            print(form)
            
            
            total_bins = request.POST.getlist('inputCodigo')
            print(total_bins)

            total_bin = request.POST.getlist('inputProducto')
            print(total_bin)

            total_bi = request.POST.getlist('inputCantidad')
            print(total_bi)
            

            contador = request.POST.get("contador")
            print (contador)
            print("llega al POST")
            form = PedidoNuevoForm(request.POST,request.FILES)

            
            idpedidoNuevo = Pedido.objects.count()+1
            try:
                pedido = Pedido.objects.get(idpedido =idpedidoNuevo).idpedido 
                while pedido != NULL:
                    idpedidoNuevo = idpedidoNuevo +10
                    pedido = Pedido.objects.get(idpedido =idpedidoNuevo).idpedido 
            except:
                idpedidoNuevo =idpedidoNuevo

            print(idpedidoNuevo)

            agregarPedido(idpedidoNuevo,form)


            contador = int(request.POST.get("contador"))
            ciclo = 0
            print (contador)

            #for total_bins in range(contador):
                #agregarPedidoProducto(idpedidoNuevo,total_bins[ciclo],1,total_bi[ciclo])
                #ciclo +=1
            while ciclo < contador:
                agregarPedidoProducto(idpedidoNuevo,total_bins[ciclo],(ciclo+1),total_bi[ciclo])
                #print("el ciclo es"+ciclo)
                ciclo=ciclo +1

            #print("fueron " + ciclo+" inserts")

            store = request.COOKIES['store']
            print (proveedor)
            
            template_path = 'core/pdf/pedidopdf.html'
            proveedor = Proveedor.objects.get(idproveedor=proveedor)
            empresa = Empresa.objects.get(nmbempresa=proveedor.rutempresa)
            almacen = Almacen.objects.get(idalmacen=store)
            pedido= Pedido.objects.get(idpedido=idpedidoNuevo)
            pedidoLine = PedidoLine.objects.filter(idpedido=idpedidoNuevo)

            detalle=[]
            sumaTotal= 0
            for fila in pedidoLine:
                detalle1=[]
                detalle1.append(fila.lineid)
                codigo=fila.codigo
                detalle1.append(codigo)
                nombreProducto=Producto.objects.get(codigo=fila.codigo).nmbproducto
                detalle1.append(nombreProducto)
                detalle1.append(fila.cantidad)
                producto = Producto.objects.get(codigo=fila.codigo).preciocompra
                
                productoCant = fila.cantidad * producto
                sumaTotal=sumaTotal + productoCant
                detalle1.append(producto)
                detalle1.append(productoCant)
                detalle.append(detalle1)
            
            neto=  round(sumaTotal/1.19)
            iva = round(neto * 0.19)
            context = {'proveedor': proveedor,'almacen':almacen,'pedido':pedido,'detalle':detalle,'empresa':empresa,'sumaTotal':sumaTotal,'neto':neto,'iva':iva}
            
            # Create a Django response object, and specify content_type as pdf
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="NroPedido'+ str(idpedidoNuevo)+'.pdf"'
            # find the template and render it.
            template = get_template(template_path)
            html = template.render(context)

            # create a pdf
            pdf = pisa.CreatePDF(
                html, dest=response)
            
            # if error then show some funny view
            if pdf.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response
            
                    
            
        data ={
                'tipo_usuario': request.COOKIES['tipo_usuario'],
                'login_status': request.COOKIES['login_status'],
                'store': request.COOKIES['store'],
                'nmbusuario': request.COOKIES['nmbusuario'],
                'apellidousuario': request.COOKIES['apellidousuario'],
                'proveedor':proveedor,
            } 
    else:
        data = {
        'tipo_usuario': 6666,
        'login_status': False,
        }         
    
    return render(request,'core/pedidoNew.html',data)

def generarPDF(request,idpedido):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        store= request.COOKIES['store']
        template_path = 'core/pdf/pedidopdf.html'       
        
        almacen = Almacen.objects.get(idalmacen=store)
        pedido= Pedido.objects.get(idpedido=idpedido)
        pedidoLine = PedidoLine.objects.filter(idpedido=idpedido)

        for fila in pedidoLine:
            codProveedor = fila.codigo

        proveedor = Producto.objects.get(codigo=codProveedor).idproveedor
        empresa = Empresa.objects.get(nmbempresa=proveedor.rutempresa)
        detalle=[]
        sumaTotal= 0
        for fila in pedidoLine:
            detalle1=[]
            detalle1.append(fila.lineid)
            codigo=fila.codigo
            detalle1.append(codigo)
            nombreProducto=Producto.objects.get(codigo=fila.codigo).nmbproducto
            detalle1.append(nombreProducto)
            detalle1.append(fila.cantidad)
            producto = Producto.objects.get(codigo=fila.codigo).preciocompra
            
            productoCant = fila.cantidad * producto
            sumaTotal=sumaTotal + productoCant
            detalle1.append(producto)
            detalle1.append(productoCant)
            detalle.append(detalle1)
        
        neto=  round(sumaTotal/1.19)
        iva = round(neto * 0.19)
        context = {'proveedor': proveedor,'almacen':almacen,'pedido':pedido,'detalle':detalle,'empresa':empresa,'sumaTotal':sumaTotal,'neto':neto,'iva':iva}
        
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="NroPedido'+ str(idpedido)+'.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pdf = pisa.CreatePDF(
            html, dest=response)
        
        # if error then show some funny view
        if pdf.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response

#OSCAR
def pedido_producto(request):
    prov = request.GET.get('idproveedor')
    data ={
        'producto': Producto.objects.filter(idproveedor = prov)
    }
    return render(request, 'core/cbxProductoProveedor.html', data)

def pedido_update1(request, idpedido):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        pedido = Pedido.objects.get(idpedido = idpedido)
        form = Pedido1Forms(instance = pedido)
        res=int(Pedido.objects.get(idpedido = idpedido).pedidoanulado)
        cas = int(res)

        if cas != 0:           
            if request.method == 'POST':
                form = Pedido1Forms(request.POST,request.FILES,instance=pedido)
                if form.is_valid():
                    
                    form.save()                   
                    return redirect(reverse('pedidoMenu')+ "?ok")
                else:
                    return redirect(reverse('pedidoUpdate1') + idpedido)
        else:
            return redirect(reverse('pedidoMenu')+ "?failanulado")
        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'form':form,
            'cas':cas,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        } 
    else:
        data = {
        'tipo_usuario': 6666,
        'login_status': False,
    }  
    

    return render(request,'core/pedidoUpdate1.html',data)
    



def pedido_update(request, idpedido):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        pedido = Pedido.objects.get(idpedido = idpedido)
        pedidoLine =PedidoLine.objects.filter(idpedido=idpedido)

        for fila in pedidoLine:
            codProveedor = fila.codigo

        proveedor = Producto.objects.get(codigo=codProveedor).idproveedor

        emailProveedor=Proveedor.objects.get(nmbproveedor=proveedor).email

        
        if request.method == 'POST':
            file = request.POST.get('file')
            if file != '':
                filepdf= request.FILES['file']   
                send_email(emailProveedor,filepdf,pedido.idpedido)
            
            #send_email(email,file)
         
        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'pedido':pedido,
            'pedidoLine':pedidoLine,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        } 
    else:
        data = {
        'tipo_usuario': 6666,
        'login_status': False,
    }  
    

    return render(request,'core/pedidoUpdate.html',data)
#------BODEGA-----------------------
def menuBodega(request):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:

        bodega = Bodega.objects.all()


        page = request.GET.get('page',1)
        paginator = Paginator(bodega,5)

        try :
            bodega = paginator.page(page)
        except PageNotAnInteger :
            bodega = paginator.page(1)
        except EmptyPage:
            bodega = paginator.page(paginator.num_pages)

        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'bodega':bodega,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        } 
    else:
        data = {
        'tipo_usuario': 6666,
        'login_status': False,
    }  
    return render(request,"core/bodegaMenu.html",data) 

        

def bodega_New(request):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
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
        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'form':form,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        } 
    else:
        data = {
        'tipo_usuario': 6666,
        'login_status': False,
    }         
   

    return render(request,'core/bodegaNew.html',data)

def bodega_delete(request, idbodega):
    producto = Bodega.objects.get(idbodega = idbodega)
    try:
        producto.delete()
        return redirect(to="bodegaMenu")
    except:
        return redirect(reverse('bodegaMenu')+ "?errorPK")
    

def bodega_update(request, idbodega):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        bodega = Bodega.objects.get(idbodega = idbodega)
        form = BodegaForm(instance = bodega)

        if request.method == 'POST':
            form = BodegaForm(request.POST,request.FILES,instance=bodega)
            if form.is_valid():
                form.save()                
                return redirect(reverse('bodegaMenu')+ "?ok")
            else:
                return redirect(reverse('bodegaUpdate')+ idbodega)
        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'form':form,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        } 
    else:
        data = {
        'tipo_usuario': 6666,
        'login_status': False,
    }  
    

    return render(request,'core/bodegaUpdate.html',data)

#----------------------------------

#------USUARIO---------------------
def menuEmpleado(request):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        cuentaUsuario = CuentaUsuario.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(cuentaUsuario,5)

        try :
            cuentaUsuario = paginator.page(page)
        except PageNotAnInteger :
            cuentaUsuario = paginator.page(1)
        except EmptyPage:
            cuentaUsuario = paginator.page(cuentaUsuario.num_pages)
        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'cuentaUsuario':cuentaUsuario,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        }  
    else:
        data = {
        'tipo_usuario': 6666,
        'login_status': False,
    }  
    return render(request,"core/empleadoMenu.html",data)

def empleado_New(request):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        if request.method == 'POST':
            form = EmpleadosForm(request.POST or None,request.FILES or None)
            if form.is_valid():
                print("pasa")        
                rutusuario =form.cleaned_data.get("rutusuario")
                apellidousuario = form.cleaned_data.get("apellidousuario")
                nmbusuario = form.cleaned_data.get("nmbusuario")
                email = form.cleaned_data.get("email")
                idalmacen=form.cleaned_data.get("idalmacen")
                
                rutusuario =form.cleaned_data.get("rutusuario")
                apellidousuario = form.cleaned_data.get("apellidousuario")
                nmbusuario = form.cleaned_data.get("nmbusuario")
                email = form.cleaned_data.get("email")
                idalmacen=form.cleaned_data.get("idalmacen")
                
                nidalmacen = Almacen.objects.get(nmbalmacen=idalmacen)
                print(nidalmacen)
                #crearUsuario(rutusuario,2,nidalmacen.idalmacen,nmbusuario.upper(),apellidousuario.upper(),email)
                #send_emailNewEmpleado(email,rutusuario)   
    
                return redirect(reverse('empleadoMenu')+ "?ok")
            else:
                return redirect(reverse('empleadoNew')+ "?fail")
        else:
            form = EmpleadosForm()
        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'form':form,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        }  
    else:
        data = {
        'tipo_usuario': 6666,
        'login_status': False,
    }       


    return render(request,'core/empleadoNew.html',data)

def empleado_delete(request, rutusuario):
    cuentaUsuario = CuentaUsuario.objects.get(rutusuario = rutusuario)
    try:
        cuentaUsuario.delete()
        return redirect(to="empleadoMenu")
    except:
       return redirect(reverse('empleadoMenu')+ "?errorPK")
       

def empleado_updateAdmin(request, rutusuario):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        cuentaUsuario = CuentaUsuario.objects.get(rutusuario = rutusuario)
        form = EmpleadosForm(instance = cuentaUsuario)

        if request.method == 'POST':
            form = EmpleadosForm(request.POST,request.FILES,instance=cuentaUsuario)
            if form.is_valid():
                form.save()                
                return redirect(reverse('empleadoMenu')+ "?ok")
            else:
                return redirect(reverse('empleadoUpdateAdmin')+ rutusuario)
        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'form':form,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        }  
    else:
        data = {
        'tipo_usuario': 6666,
        'login_status': False,
    }  
    

    return render(request,'core/empleadoUpdateAdmin.html',data)

def empleado_update(request, idproveedor):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        proveedor = Proveedor.objects.get(idproveedor = idproveedor)
        form = ProveedorForm(instance = proveedor)

        if request.method == 'POST':
            form = ProveedorForm(request.POST,request.FILES,instance=proveedor)
            if form.is_valid():
                form.save()                
                return redirect(reverse('empleadoMenu')+ "?ok")
            else:
                return redirect(reverse('proveedorUpdate')+ idproveedor)

        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'form':form,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        }  
    else:
        data = {
        'tipo_usuario': 6666,
        'login_status': False,
    }  
   
    return render(request,'core/proveedorUpdate.html',data)

#--------------------------------
#EMPRESA
def menuEmpresa(request):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        empresa = Empresa.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(empresa,5)

        try :
            empresa = paginator.page(page)
        except PageNotAnInteger :
            empresa = paginator.page(1)
        except EmptyPage:
            empresa = paginator.page(empresa.num_pages)
        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'empresa':empresa,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        } 
    else:
            data = {
            'tipo_usuario': 6666,
            'login_status': False,
        }  
    return render(request,"core/empresaMenu.html",data)

def empresa_New(request):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        if request.method == 'POST':
            form = EmpresaForm(request.POST or None,request.FILES or None)
            if form.is_valid():
                rutempresa = form.cleaned_data.get("rutempresa")
                nmbempresa = form.cleaned_data.get("nmbempresa")    
                direccion = form.cleaned_data.get("direccion")   
                idcomuna = form.cleaned_data.get("idcomuna")           
                obj = Empresa.objects.create(
                    rutempresa=rutempresa,
                    nmbempresa=nmbempresa,
                    direccion=direccion,
                    idcomuna=idcomuna,
                )

                obj.save()           
                return redirect(reverse('empresaMenu')+ "?ok")
            else:
                return redirect(reverse('empresaNew')+ "?fail")
       
        else:
            form = EmpresaForm()

        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'form':form,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        } 
    else:
        data = {
            'tipo_usuario': 6666,
            'login_status': False,
            }          
    
    return render(request,'core/empresaNew.html',data)

def empresa_delete(request, rutempresa):
    empresa = Empresa.objects.get(rutempresa = rutempresa)
    try:
        empresa.delete()
        return redirect(to="empresaMenu")
    except:
        return redirect(reverse('empresaMenu')+ "?errorPK")
    

def empresa_update(request, rutempresa):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        empresa = Empresa.objects.get(rutempresa = rutempresa)
        form = EmpresaForm(instance = empresa)

        if request.method == 'POST':
            form = EmpresaForm(request.POST,request.FILES,instance=empresa)
            if form.is_valid():
                form.save()                
                return redirect(reverse('empresaMenu')+ "?ok")
            else:
                return redirect(reverse('empresaUpdate')+ rutempresa)
        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'form':form ,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        } 
    else:
            data = {
            'tipo_usuario': 6666,
            'login_status': False,
        }  
    

    return render(request,'core/empresaUpdate.html',data)


def pdfCorreo(request):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
       
        if request.method == 'POST':
            pp= request.POST.get('pp')
            email = CuentaUsuario.objects.get(rutusuario=pp).email
            file = request.FILES['file']              
            #send_email(email,pp,file)
        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        } 
    else:
            data = {
            'tipo_usuario': 6666,
            'login_status': False,
        }  
    

    return render(request,'core/list.html',data)


#---------recepcion

def menuRecepcion(request):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        empresa = Empresa.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(empresa,5)

        try :
            empresa = paginator.page(page)
        except PageNotAnInteger :
            empresa = paginator.page(1)
        except EmptyPage:
            empresa = paginator.page(empresa.num_pages)
        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'empresa':empresa,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        } 
    else:
            data = {
            'tipo_usuario': 6666,
            'login_status': False,
        }  
    return render(request,"core/recepcionMenu.html",data)

def recepcion_New(request):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        if request.method == 'POST':
            form = EmpresaForm(request.POST or None,request.FILES or None)
            if form.is_valid():
                rutempresa = form.cleaned_data.get("rutempresa")
                nmbempresa = form.cleaned_data.get("nmbempresa")    
                direccion = form.cleaned_data.get("direccion")   
                idcomuna = form.cleaned_data.get("idcomuna")           
                obj = Empresa.objects.create(
                    rutempresa=rutempresa,
                    nmbempresa=nmbempresa,
                    direccion=direccion,
                    idcomuna=idcomuna,
                )

                obj.save()           
                return redirect(reverse('empresaMenu')+ "?ok")
            else:
                return redirect(reverse('empresaNew')+ "?fail")
       
        else:
            form = EmpresaForm()

        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'form':form,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        } 
    else:
        data = {
            'tipo_usuario': 6666,
            'login_status': False,
            }          
    
    return render(request,'core/recepcionNew.html',data)

def recepcion_delete(request, rutempresa):
    empresa = Empresa.objects.get(rutempresa = rutempresa)
    try:
        empresa.delete()
        return redirect(to="recepcionMenu")
    except:
        return redirect(reverse('recepcionMenu')+ "?errorPK")
    

def recepcion_update(request, rutempresa):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        empresa = Empresa.objects.get(rutempresa = rutempresa)
        form = EmpresaForm(instance = empresa)

        if request.method == 'POST':
            form = EmpresaForm(request.POST,request.FILES,instance=empresa)
            if form.is_valid():
                form.save()                
                return redirect(reverse('empresaMenu')+ "?ok")
            else:
                return redirect(reverse('empresaUpdate')+ rutempresa)
        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'form':form ,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        } 
    else:
            data = {
            'tipo_usuario': 6666,
            'login_status': False,
        }  
    

    return render(request,'core/recepcionUpdate.html',data)



#----SUCURSAL
def menuSucursal(request):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        almacen = Almacen.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(almacen,5)

        try :
            almacen = paginator.page(page)
        except PageNotAnInteger :
            almacen = paginator.page(1)
        except EmptyPage:
            almacen = paginator.page(almacen.num_pages)
        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'almacen':almacen,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        } 
    else:
            data = {
            'tipo_usuario': 6666,
            'login_status': False,
        }  
    return render(request,"core/sucursalMenu.html",data)

def sucursal_New(request):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        if request.method == 'POST':
            form = AlmacenForm(request.POST or None,request.FILES or None)
            if form.is_valid():
                idcomuna = form.cleaned_data.get("idcomuna")
                idalmacen = form.cleaned_data.get("idalmacen")    
                direccion = form.cleaned_data.get("direccion")   
                nmbalmacen = form.cleaned_data.get("nmbalmacen")           
                obj = Almacen.objects.create(
                    idcomuna=idcomuna,
                    nmbalmacen=nmbalmacen,
                    direccion=direccion,
                    idalmacen=idalmacen,
                )

                obj.save()           
                return redirect(reverse('sucursalMenu')+ "?ok")
            else:
                return redirect(reverse('sucursalNew')+ "?fail")
       
        else:
            form = AlmacenForm()

        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'form':form,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        } 
    else:
        data = {
            'tipo_usuario': 6666,
            'login_status': False,
            }          
    
    return render(request,'core/sucursalNew.html',data)

def sucursal_delete(request, idalmacen):
    empresa = Almacen.objects.get(idalmacen = idalmacen)
    try:
        empresa.delete()
        return redirect(to="sucursalMenu")
    except:
        return redirect(reverse('sucursalMenu')+ "?errorPK")
    

def sucursal_update(request, idalmacen):
    if 'tipo_usuario' in request.COOKIES and 'login_status' in request.COOKIES and 'store' in request.COOKIES:
        empresa = Almacen.objects.get(idalmacen = idalmacen)
        form = AlmacenForm(instance = empresa)

        if request.method == 'POST':
            form = AlmacenForm(request.POST,request.FILES,instance=empresa)
            if form.is_valid():
                form.save()                
                return redirect(reverse('sucursalMenu')+ "?ok")
            else:
                return redirect(reverse('sucursalUpdate')+ idalmacen)
        data ={
            'tipo_usuario': request.COOKIES['tipo_usuario'],
            'login_status': request.COOKIES['login_status'],
            'store': request.COOKIES['store'],
            'form':form ,
            'nmbusuario': request.COOKIES['nmbusuario'],
            'apellidousuario': request.COOKIES['apellidousuario'],
        } 
    else:
            data = {
            'tipo_usuario': 6666,
            'login_status': False,
        }  
    

    return render(request,'core/sucursalUpdate.html',data)


def pedidopdf(request):
    return render(request,'core/pdf/pedidopdf.html')

