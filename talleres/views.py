from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def registro(request):
    return render(request,'core/registro.html')

def login(request):
    return render(request,'core/login.html')

def LogueadoTalleresUsuario(request):
    return render(request,'core/LogueadoTalleresUsuario.html')

def InscripcionTalleresUsuario(request):
    return render(request,'core/InscripcionTalleresUsuario.html')

def muestraDatosUsuario(request):
    return render(request,'core/muestraDatosUsuario.html')

def EliminarTallerUsuario(request):
    return render(request, 'core/EliminarTallerUsuario.html')

def evaluarTallerUsuario(request):
    return render(request, 'core/evaluarTallerUsuario.html')