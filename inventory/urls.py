from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio, name='inicio'),
    path('productos',productos, name='productos'),
    path('producto/<int:producto_pk>',producto_detalle, name='producto_detalle'),
]
