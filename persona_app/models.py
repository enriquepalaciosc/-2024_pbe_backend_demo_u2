from django.db import models

# Create your models here.
class Persona(models.Model):
    # id, nombre, edad, habilitada
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    habilitada = models.BooleanField(null=True, default=0)
    # 0 = False / 1 = True
    # MySQL/MariaDB no tiene BOOLEAN directo con True o False
    fecha_nacimiento = models.DateField(null=True)
