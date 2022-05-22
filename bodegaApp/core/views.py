from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"core/index.html")

def registroUsuario(request):
    return render(request,"core/registroUsuario.html")

def pedidoRealizar(request):
    return render(request,"core/pedidoRealizar.html")