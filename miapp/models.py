from django.db import models

# Create your models here.

class Socio(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=50)
    apellidop = models.CharField(max_length=50)
    apellidom = models.CharField(max_length=50)
    direccion = models.CharField(max_length=60)
    comuna = models.CharField(max_length=60)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    region = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return f"{self.nombre} {self.apellidop}"