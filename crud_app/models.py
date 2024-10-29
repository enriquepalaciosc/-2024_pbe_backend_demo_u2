from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    precio = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    # cliente = models.ManyToManyField(Cliente)

class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    habilitado = models.BooleanField(null=True, default=0)

    # relación n..m
    producto = models.ManyToManyField(Producto)

class Credencial(models.Model):
    id = models.BigAutoField(primary_key=True)
    serie = models.CharField(max_length=20)
    fecha_emision = models.DateField(null=True)

    # relación 1..1 (se aplica en credencial al ser dependiente de cliente)
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
