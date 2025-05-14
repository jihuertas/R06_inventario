from django import forms
from .models import *
from django.core.exceptions import ValidationError


# class ProductoForm (forms.Form):
#     nombre = forms.CharField(max_length=50, label='Nombre del producto:')
#     descripcion = forms.CharField(max_length=250)
#     stock = forms.IntegerField()
#     precio = forms.DecimalField(max_digits=9, decimal_places=2)

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields= ['nombre', 'descripcion', 'stock', 'precio', 'categoria']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields= ['nombre']

    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']

        #Validamos que el nombre no exista       
        if Categoria.objects.filter(nombre=nombre).exists():
            raise ValidationError("La categoría ya existe")
        return nombre
 
    
