from django import forms

class ProductoForm (forms.Form):
    nombre = forms.CharField(max_length=50, label='Nombre del producto:')
    descripcion = forms.CharField(max_length=250)
    stock = forms.IntegerField()
    precio = forms.DecimalField(max_digits=9, decimal_places=2)
