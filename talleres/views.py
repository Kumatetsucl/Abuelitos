from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from .models import * 
from datetime import date
from django.contrib.auth.decorators import user_passes_test, login_required


# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def es_administrador(user):
    return user.is_authenticated and user.is_staff

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
            if user.is_staff:
                return redirect('loagueadoTalleresAdmin')
            else:
                return redirect('LogueadoTalleresUsuario')
        else:
            messages.error(request, 'Error nombre de usuario o contraseña incorrectos')
            return render(request, 'core/login.html')
    else:
        return render(request, 'core/login.html')

def cerrar_sesion(request):
    logout(request)
    if 'username' in request.session:
        del request.session['username']  
    
    return redirect('index') 

@login_required
def LogueadoTalleresUsuario(request):
    usuario = CustomUser.objects.get(id=request.user.id)
    talleres_inscritos = usuario.talleres_inscritos.all()
    
    return render(request, 'core/LogueadoTalleresUsuario.html', {'talleres_inscritos': talleres_inscritos})

@login_required
def InscripcionTalleresUsuario(request):
    talleres = Tallere.objects.all()
    if request.method == 'POST':
        taller_id = request.POST.get('taller')
        taller = get_object_or_404(Tallere, id=taller_id)
        request.user.talleres_inscritos.add(taller)
        return redirect('LogueadoTalleresUsuario')
    else:
        talleres = Tallere.objects.all()
        return render(request, 'core/InscripcionTalleresUsuario.html', {'talleres': talleres})

@login_required
def muestraDatosUsuario(request):
    return render(request,'core/muestraDatosUsuario.html')

@login_required
def EliminarTallerUsuario(request):
    usuario = CustomUser.objects.get(id=request.user.id)
    talleres_inscritos = usuario.talleres_inscritos.all()
    return render(request,'core/EliminarTallerUsuario.html', {'talleres_inscritos': talleres_inscritos})
    

@login_required
def eliminar_taller_usuario(request, taller_id):
    taller = get_object_or_404(Tallere, id=taller_id)
    usuario = CustomUser.objects.get(id=request.user.id)
    if taller in usuario.talleres_inscritos.all():
        usuario.talleres_inscritos.remove(taller)
        messages.success(request, 'Inscripción retirada exitosamente.')
        return redirect('EliminarTallerUsuario')
    else:
        messages.error(request, 'El usuario no está inscrito en este taller.')

@login_required
def evaluarTallerUsuario(request):
    return render(request, 'core/evaluarTallerUsuario.html')

####################################################################################################################

@user_passes_test(es_administrador)
def loagueadoTalleresAdmin(request):
    talleres = Tallere.objects.all()
    return render(request,'core/mantenedores/tallerFuncionario/loagueadoTalleresAdmin.html', {'talleres': talleres})

@user_passes_test(es_administrador)
def administrarTalleresFuncionario(request):
    talleres = Tallere.objects.all()
    return render(request,'core/mantenedores/tallerFuncionario/administrarTalleresFuncionario.html', {'talleres': talleres})

@user_passes_test(es_administrador)
def crearTallerFuncionario(request):
    instructores = Instructore.objects.all()
    if request.method == 'POST':
        formulario = TallerForm(request.POST)
        if formulario.is_valid():
            nuevo_taller = formulario.save(commit=False)
            nuevo_taller.lunes = request.POST.get('lunes', False) == 'on'
            nuevo_taller.martes = request.POST.get('martes', False) == 'on'
            nuevo_taller.miercoles = request.POST.get('miercoles', False) == 'on'
            nuevo_taller.jueves = request.POST.get('jueves', False) == 'on'
            nuevo_taller.viernes = request.POST.get('viernes', False) == 'on'
            nuevo_taller.sabado = request.POST.get('sabado', False) == 'on'
            nuevo_taller = formulario.save()
            messages.success(request, 'Taller creado exitosamente.')
            return redirect('administrarTalleresFuncionario')  # Redirige a la vista que muestra los talleres
        else:
            errors = dict((field, errors[0]) for field, errors in formulario.errors.items())
            print(errors)
    else:
        formulario = TallerForm()
        
    return render(request,'core/mantenedores/tallerFuncionario/crearTallerFuncionario.html', {'form': formulario, 'instructores': instructores})

@user_passes_test(es_administrador)
def modificarTallerFuncionario(request, taller_id):
    taller = get_object_or_404(Tallere, id=taller_id)

    if request.method == 'POST':
        formulario = TallerForm(request.POST, instance=taller)
        if formulario.is_valid():
            taller = formulario.save(commit=False)
            taller.lunes = request.POST.get('lunes', False) == 'on'
            taller.martes = request.POST.get('martes', False) == 'on'
            taller.miercoles = request.POST.get('miercoles', False) == 'on'
            taller.jueves = request.POST.get('jueves', False) == 'on'
            taller.viernes = request.POST.get('viernes', False) == 'on'
            taller.sabado = request.POST.get('sabado', False) == 'on'
            formulario.save()
            messages.success(request, 'Taller modificado exitosamente.')
            return redirect('administrarTalleresFuncionario') 
        else:
            errors = dict((field, errors[0]) for field, errors in formulario.errors.items())
            print(errors)
            messages.error(request, 'Error al modificar el taller. Por favor, verifica los datos ingresados.')
    else:
        formulario = TallerForm(instance=taller)

    instructores = Instructore.objects.all()
    return render(request, 'core/mantenedores/tallerFuncionario/modificarTallerFuncionario.html', {'form': formulario, 'instructores': instructores, 'taller': taller})

@user_passes_test(es_administrador)
def eliminar_taller(request, taller_id):
    taller = get_object_or_404(Tallere, id=taller_id)
    taller.delete()
    # Puedes agregar un mensaje de éxito si lo deseas
    messages.success(request, 'Taller eliminado exitosamente.')
    return redirect('administrarTalleresFuncionario')

####################################################################################################################

@user_passes_test(es_administrador)
def administrarUsuariosFuncionario(request):
    usuarios = CustomUser.objects.all()
    # Calcular la edad y agregarla al contexto
    for usuario in usuarios:
        if usuario.fecha_nacimiento:
            hoy = date.today()
            edad = hoy.year - usuario.fecha_nacimiento.year - ((hoy.month, hoy.day) < (usuario.fecha_nacimiento.month, usuario.fecha_nacimiento.day))
            usuario.edad = edad
    
    return render(request,'core/mantenedores/usuarioFuncionario/administrarUsuariosFuncionario.html', {'usuarios': usuarios})

@user_passes_test(es_administrador)
def crearUsuariosFuncionario(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.username = user.email  
            password = form.cleaned_data.get('password')
            user.set_password(password) 
            user.save()  
            messages.success(request, f'¡Cuenta creada exitosamente!')
            return redirect('administrarUsuariosFuncionario') 
    else:
        form = UserForm()
    return render(request, 'core/mantenedores/usuarioFuncionario/crearUsuariosFuncionario.html', {'form': form})

@user_passes_test(es_administrador)
def modificarUsuarioFuncionario(request, usuario_id):
    usuario = get_object_or_404(CustomUser, id=usuario_id)
    if request.method == 'POST':
        formulario = UserForm(request.POST, instance=usuario)
        if formulario.is_valid():
            usuario = formulario.save(commit=False)
            nueva_contrasena = formulario.cleaned_data.get('password')
            if nueva_contrasena:
                usuario.set_password(nueva_contrasena)
            usuario.save()
            messages.success(request, 'Usuario modificado exitosamente.')
            return redirect('administrarUsuariosFuncionario')
        else:
            errors = dict((field, errors[0]) for field, errors in formulario.errors.items())
            print(errors)
    else:
        formulario = UserForm(instance=usuario)
        
    return render(request, 'core/mantenedores/usuarioFuncionario/modificarUsuarioFuncionario.html', {'form': formulario, 'usuario': usuario})

@user_passes_test(es_administrador)
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(CustomUser, id=usuario_id)
    usuario.delete()
    # Puedes agregar un mensaje de éxito si lo deseas
    messages.success(request, 'Usuario eliminado exitosamente.')
    return redirect('administrarUsuariosFuncionario')


####################################################################################################################

@user_passes_test(es_administrador)
def administrarInstructorFuncionario(request):
    instructores = Instructore.objects.all()
    return render(request,'core/mantenedores/instructorFuncionario/administrarInstructorFuncionario.html', {'instructores': instructores})

@user_passes_test(es_administrador)
def crearInstructorFuncionario(request):
    return render(request,'core/mantenedores/instructorFuncionario/crearInstructorFuncionario.html')

@user_passes_test(es_administrador)
def modificarInstructorFuncionario(request):
    return render(request,'core/mantenedores/instructorFuncionario/modificarInstructorFuncionario.html')

####################################################################################################################

@user_passes_test(es_administrador)
def inscribir(request):
    return render(request,'core/mantenedores/InscribirATaller/Inscribir.html')

####################################################################################################################
@login_required
def muestraDatosUsuario(request):
    return render(request,'core/muestraDatosUsuario.html')

@user_passes_test(es_administrador)
def muestraDatosFuncionario(request):
    return render(request,'core/muestraDatosFuncionario.html')