from django.shortcuts import redirect, render
from .models import Producto
from .forms import ProductoForm

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

def producto_nuevo(request):

    if request.method == 'POST':
        formulario = ProductoForm(request.POST)

        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            descripcion = formulario.cleaned_data['descripcion']
            stock = formulario.cleaned_data['stock']
            precio = formulario.cleaned_data['precio']

            Producto.objects.create(nombre=nombre, descripcion=descripcion, stock=stock, precio=precio)
            return redirect('productos')

    else:
        formulario = ProductoForm()
        return render(request, 'inventory/producto_nuevo.html',{'form':formulario})

def producto_editar(request, producto_pk):
    producto = Producto.objects.get(pk=producto_pk)

    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            descripcion = formulario.cleaned_data['descripcion']
            stock = formulario.cleaned_data['stock']
            precio = formulario.cleaned_data['precio']

            producto.nombre = nombre
            producto.descripcion = descripcion
            producto.stock = stock
            producto.precio = precio

            producto.save()
            return redirect('productos')

    else:   
        datos_producto = {'nombre': producto.nombre, 'descripcion': producto.descripcion, 'stock':producto.stock, 'precio':producto.precio}
        formulario = ProductoForm(initial=datos_producto)

    return render(request, 'inventory/producto_editar.html',{'form':formulario})