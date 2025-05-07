from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio, name='inicio'),
    path('productos',productos, name='productos'),
    path('producto/<int:producto_pk>',producto_detalle, name='producto_detalle'),
    path('producto/<int:producto_pk>/editar',producto_editar, name='producto_editar'),
    path('producto/nuevo',producto_nuevo, name='producto_nuevo'),
]
