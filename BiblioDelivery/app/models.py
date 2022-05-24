from django.db import models
import datetime
# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id Categoria')
    nombreCategoria = models.CharField(max_length=20,verbose_name='Nombre Categoria')
    def __str__(self):
        return self.nombreCategoria
class Producto(models.Model):
    codigoProducto = models.IntegerField(primary_key=True,max_length=10,verbose_name='Codigo Producto')
    nombreProducto = models.CharField(max_length=20,verbose_name='Nombre Producto')
    precioProducto = models.IntegerField(max_length=7,verbose_name='Precio Producto')
    categoriaProducto = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagenProducto = models.ImageField(upload_to="static",null=True)
    def __str__(self):
        return self.nombreProducto

class Cliente(models.Model):
    rutCliente = models.IntegerField(primary_key=True,max_length=9,verbose_name='Rut cliente')
    nombreCliente = models.CharField(max_length=20,verbose_name='Nombre Cliente')
    direccionCliente= models.CharField(max_length=20,verbose_name='Direccion Cliente')
    numeroCliente= models.IntegerField(max_length=9,verbose_name='Numero Cliente')
    emailCliente = models.EmailField(verbose_name='Correo Cliente')
    fechanacimientoCliente=models.DateField(verbose_name='Fecha Nacimiento Cliente')
    def __str__(self):
        return self.rutCliente
