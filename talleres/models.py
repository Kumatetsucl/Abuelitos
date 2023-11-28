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
    
