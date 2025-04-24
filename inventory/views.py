from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'inventory/inicio.html')

def productos(request):
    return render(request, 'inventory/productos.html')