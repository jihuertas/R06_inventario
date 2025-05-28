from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio, name='inicio'),
    path('productos',ProductoListView.as_view(), name='productos'),
    path('producto/<int:producto_pk>',ProductoDetailView.as_view(), name='producto_detalle'),
    path('producto/<int:producto_pk>/borrar',ProductoDeleteView.as_view(), name='producto_borrar'),
    path('producto/<int:pk>/editar/<int:articulo_pk>',ProductoEditarView.as_view(), name='producto_editar'),
    path('producto/nuevo',ProductoCrearView.as_view(), name='producto_nuevo'),
    
    #path('categoria/nueva', categoria_nueva, name='categoria_nueva'),
]
