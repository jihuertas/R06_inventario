from django.shortcuts import render
from .models import Producto

# Create your views here.
def inicio(request):
    return render(request,'inventory/inicio.html')

#CRUD PRODUCTOS

# Listado de productos
def productos(request):
    productos_todos = Producto.objects.all()
    return render(request, 'inventory/productos.html',{'productos':productos_todos})

# Detalle de producto
def producto_detalle(request, producto_pk):
    producto_detalle = Producto.objects.get(pk=producto_pk)
    return render(request, 'inventory/producto_detalle.html',{'producto':producto_detalle})