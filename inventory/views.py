from django.shortcuts import redirect, render

from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm

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
            # nombre = formulario.cleaned_data['nombre']
            # descripcion = formulario.cleaned_data['descripcion']
            # stock = formulario.cleaned_data['stock']
            # precio = formulario.cleaned_data['precio']

            # Producto.objects.create(nombre=nombre, descripcion=descripcion, stock=stock, precio=precio)
            formulario.save()
            return redirect('productos')

    else:
        form_producto = ProductoForm()
        form_categoria = CategoriaForm()
        return render(request, 'inventory/producto_nuevo.html',{'form_producto':form_producto, 'form_categoria': form_categoria})

def producto_editar(request, producto_pk):
    producto = Producto.objects.get(pk=producto_pk)

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance=producto)
        if formulario.is_valid():
            # nombre = formulario.cleaned_data['nombre']
            # descripcion = formulario.cleaned_data['descripcion']
            # stock = formulario.cleaned_data['stock']
            # precio = formulario.cleaned_data['precio']

            # if producto.nombre != nombre:
            #     producto.nombre = nombre

            # producto.descripcion = descripcion
            # producto.stock = stock
            # producto.precio = precio

            # producto.save()
            formulario.save()
            return redirect('productos')

    else:   
        # datos_producto = {'nombre': producto.nombre, 'descripcion': producto.descripcion, 'stock':producto.stock, 'precio':producto.precio}
        formulario = ProductoForm(instance=producto)

    return render(request, 'inventory/producto_editar.html',{'form':formulario})

def producto_borrar(request, producto_pk):
    producto = Producto.objects.get(pk=producto_pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')
    else:
        return render(request, 'inventory/producto_borrar.html',{'producto':producto})
    

def categoria_nueva(request):
    form = CategoriaForm(request.POST)
    if form.is_valid():
        form.save()        
    form_producto = ProductoForm()
    return render(request, 'inventory/producto_nuevo.html',{'form_producto':form_producto, 'form_categoria': form})
