from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni =models.IntegerField

    def __str__(self):
         
        return f" {self.nombre} - {self.apellido} - {self.dni}"
class Producto(models.Model):
    nombre = models.CharField(max_length=25)
    precio = models.FloatField(default=0)
    stock_actual = models.IntegerField(default=0)
    proveedor = models.ForeignKey(
        Proveedor,
        related_name="productos",
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f" {self.nombre} - {self.precio} - {self.stock_actual} - {self.proveedor}"