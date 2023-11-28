from django import forms
from django.forms import ModelForm
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password', 'telefono', 'direccion', 'fecha_nacimiento']
