from django.shortcuts import render,get_object_or_404, redirect, reverse

# Create your views here.
def inicio(request):
     return render(request,"bodega/template/core/index.html")