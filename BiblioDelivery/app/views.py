from math import prod
from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
# Create your views here.
def home(request):
    return render(request,"home.html")
def mostrar(request):
    productos = Producto.objects.all()
    datos={
        'producto':productos
    }
    return render(request,"mostrar.html", datos)
def form_producto(request):
    datos ={
        'form' : ProductoForm()
    }
    if(request.method == 'POST'):
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']='Guardados Correctamente'
    return render (request,'form_producto.html',datos)
def form_mod_producto(request, id):
    productos = Producto.objects.get(codigoProducto=id)
    datos={
        'form': ProductoForm(instance=productos)
    }
    if(request.method == 'POST'):
        formulario = ProductoForm(data=request.POST, instance=productos)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Modificados Correctamente'
    return render (request,'form_mod_producto.html',datos)
def form_del_producto(request, id):
    productos = Producto.objects.get(codigoProducto=id)
    productos.delete()
    return redirect(to='home')