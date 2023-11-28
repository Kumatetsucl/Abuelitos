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
    return render(request,'core/mantenedores/inscribirATaller/inscribir.html')

####################################################################################################################

def muestraDatosUsuario(request):
    return render(request,'core/muestraDatosUsuario.html')

def muestraDatosFuncionario(request):
    return render(request,'core/muestraDatosFuncionario.html')