from distutils import core
import imp
from multiprocessing import context
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from .model import *


def render_pdf_view(request):

   template_path = 'core/pdf/pedidopdf.html'
   """ proveedor = Proveedor.objects.get(idproveedor=idproveedor)
   almacen = Almacen.objects.get(idalmacen=idalmacen)
   pedido= Pedido.objects.get(idpedido=idpedido)
   pedidoLine = PedidoLine.objects.get(idpedido=idpedido)
   producto =Producto.objects.all()
   context = {'provedor': proveedor,'almacen':almacen,'pedido':pedido,'pedidoLine':pedidoLine,'producto':producto} """
   context={'pp':'pp'}
   # Create a Django response object, and specify content_type as pdf
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="report.pdf"'
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