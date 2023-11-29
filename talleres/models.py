from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class CustomUser(AbstractUser):
    telefono = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=500, null=True)
    fecha_nacimiento = models.DateField(null=True)
    
    def __str__(self):
        return self.username

class Instructore(models.Model):
    nombre = models.CharField(max_length=255, null=True)
    apellido = models.CharField(max_length=255, null=True)
    telefono_contacto = models.CharField(max_length=255, null=True)
    direccion = models.CharField(max_length=255, null=True)
    correo_electronico = models.CharField(max_length=255, null=True)
    genero = models.CharField(max_length=255, null=True)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.nombre
    

class Tallere(models.Model):
    nombre_taller = models.CharField(max_length=255, null=True)
    seccion = models.CharField(max_length=255, null=True)
    lunes = models.BooleanField(default=False, null=True)
    martes = models.BooleanField(default=False, null=True)
    miercoles = models.BooleanField(default=False, null=True)
    jueves = models.BooleanField(default=False, null=True)
    viernes = models.BooleanField(default=False, null=True)
    sabado = models.BooleanField(default=False, null=True)
    horario_inicio = models.TimeField(null=True)
    horario_termino = models.TimeField(null=True)
    instructor = models.ForeignKey(Instructore, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.nombre_taller
    