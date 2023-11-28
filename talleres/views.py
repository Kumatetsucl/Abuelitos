from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate


# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def registro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.username = user.email  
            password = form.cleaned_data.get('password')
            user.set_password(password) 
            user.save()  
            login(request, user)
            messages.success(request, f'¡Cuenta creada exitosamente!')
            return redirect('index') 
    else:
        form = UserForm()
    return render(request, 'core/registro.html', {'form': form})

def loginIndex(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Error nombre de usuario o contraseña incorrectos')
            return render(request, 'core/login.html')
    else:
        return render(request, 'core/login.html')

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

####################################################################################################################

#crud talleres funcionmario
def loagueadoTalleresAdmin(request):
    return render(request,'core/mantenedores/tallerFuncionario/loagueadoTalleresAdmin.html')

def administrarTalleresFuncionario(request):
    return render(request,'core/mantenedores/tallerFuncionario/administrarTalleresFuncionario.html')

def crearTallerFuncionario(request):
    return render(request,'core/mantenedores/tallerFuncionario/crearTallerFuncionario.html')

def modificarTallerFuncionario(request):
    return render(request,'core/mantenedores/tallerFuncionario/modificarTallerFuncionario.html')

####################################################################################################################

#CRUD Usuarios desde funcionmario
def administrarUsuariosFuncionario(request):
    return render(request,'core/mantenedores/usuarioFuncionario/administrarUsuariosFuncionario.html')

def crearUsuariosFuncionario(request):
    return render(request,'core/mantenedores/usuarioFuncionario/crearUsuariosFuncionario.html')

def modificarUsuarioFuncionario(request):
    return render(request,'core/mantenedores/usuarioFuncionario/modificarUsuarioFuncionario.html')

####################################################################################################################

#CRUD Instructores desde funcionmario
def administrarInstructorFuncionario(request):
    return render(request,'core/mantenedores/instructorFuncionario/administrarInstructorFuncionario.html')

def crearInstructorFuncionario(request):
    return render(request,'core/mantenedores/instructorFuncionario/crearInstructorFuncionario.html')

def modificarInstructorFuncionario(request):
    return render(request,'core/mantenedores/instructorFuncionario/modificarInstructorFuncionario.html')

####################################################################################################################

# Inscribir a taller vista Funcionario
def inscribir(request):
    return render(request,'core/mantenedores/InscribirATaller/Inscribir.html')

####################################################################################################################

def muestraDatosUsuario(request):
    return render(request,'core/muestraDatosUsuario.html')

def muestraDatosFuncionario(request):
    return render(request,'core/muestraDatosFuncionario.html')