from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm
from django.contrib import messages
from django.views.generic import *

# Con CBV:

class ProductoListView(ListView):
    model = Producto
    template_name = 'inventory/productos.html'
    context_object_name = 'productos'
    ordering = ['nombre']

    def get_queryset(self):
        query = super().get_queryset()
        filtro_nombre = self.request.GET.get('nombre')
        if filtro_nombre:
            query = query.filter(nombre__icontains=filtro_nombre)
        return query

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'inventory/producto_detalle.html'
    context_object_name = 'productos'
    pk_url_kwarg = 'producto_pk'


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'inventory/producto_borrar.html'
    success_url = reverse_lazy('productos')
    pk_url_kwarg = 'producto_pk'

class ProductoEditarView(UpdateView):
    model=Producto
    template_name='inventory/producto_editar.html'
    success_url = reverse_lazy('productos')
    form_class = ProductoForm

class ProductoCrearView(CreateView):
    model=Producto
    template_name='inventory/producto_nuevo.html'
    success_url = reverse_lazy('productos')
    form_class = ProductoForm
    


# Create your views here.
def inicio(request):
    return render(request,'inventory/inicio.html')

#CRUD PRODUCTOS

# Listado de productos
def productos(request):
    filtro_nombre = request.GET.get('nombre')
    productos_todos = Producto.objects.all()
    if filtro_nombre:
        productos_todos = productos_todos.filter(nombre__icontains=filtro_nombre)

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

def producto_nuevo2(request):
    form_producto = ProductoForm()
    form_categoria = CategoriaForm()

    if request.method == 'POST':
        formulario = request.POST.get('formulario')

        if formulario == 'producto':
            form_producto = ProductoForm(request.POST)

            if form_producto.is_valid():
                form_producto.save()
                messages.success(request, "Producto creado correctamente.")

                return redirect('productos')
        elif formulario == 'categoria':
            form_categoria = CategoriaForm(request.POST)
            if form_categoria.is_valid():
                messages.success(request, "Categoría creada correctamente.")
                form_categoria.save()
        
    return render(request, 'inventory/producto_nuevo.html',{'form_producto':form_producto, 'form_categoria': form_categoria})




def producto_nuevo3(request):
    
    form_producto = ProductoForm()
    form_categoria = CategoriaForm()
    messages.info(request, "Mensaje 1")       

    if request.method == 'POST':
        formulario = request.POST.get('formulario')
        if formulario == 'producto':
            form_producto = ProductoForm(request.POST)
            if form_producto.is_valid():
                form_producto.save()
                return redirect('productos')

        elif formulario == 'categoria':
            form_categoria = CategoriaForm(request.POST)
            if form_categoria.is_valid():
                form_categoria.save()
                messages.add_message(request, messages.INFO, "Categoría creada")       

                form_categoria = CategoriaForm()
                    
    return render(request, 'inventory/producto_nuevo.html',{'form_producto':form_producto, 'form_categoria':form_categoria})


