from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    stock = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return f' {self.nombre} ({self.stock})'
    
    class Meta:
        verbose_name_plural = 'Productos'