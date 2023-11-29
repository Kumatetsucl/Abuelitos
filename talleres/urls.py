from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('registro',registro,name='registro'),
    path('login',loginIndex,name='login'),
    path('logout/', cerrar_sesion, name='logout'),
    path('accounts/login/', loginIndex, name='login'),
    path('LogueadoTalleresUsuario',LogueadoTalleresUsuario,name='LogueadoTalleresUsuario'),
    path('InscripcionTalleresUsuario',InscripcionTalleresUsuario,name='InscripcionTalleresUsuario'),

    path('EliminarTallerUsuario',EliminarTallerUsuario,name='EliminarTallerUsuario'),
    path('evaluarTallerUsuario', evaluarTallerUsuario, name='evaluarTallerUsuario'),
    
    #Vista principal Funacionario
    path('loagueadoTalleresAdmin', loagueadoTalleresAdmin, name='loagueadoTalleresAdmin'),
    
    #Crud Talleres desde la vista de los funcionarios
    path('administrarTalleresFuncionario', administrarTalleresFuncionario, name='administrarTalleresFuncionario'),
    path('crearTallerFuncionario',crearTallerFuncionario,name='crearTallerFuncionario'),
    path('modificarTallerFuncionario/<int:taller_id>/',modificarTallerFuncionario,name='modificarTallerFuncionario'),
    path('eliminar_taller/<int:taller_id>/', eliminar_taller, name='eliminar_taller'),
    
    #Crud Usuarios desde la vista de los funcionarios
    path('administrarUsuariosFuncionario', administrarUsuariosFuncionario, name='administrarUsuariosFuncionario'),
    path('crearUsuariosFuncionario',crearUsuariosFuncionario,name='crearUsuariosFuncionario'),
    path('modificarUsuarioFuncionario/<int:usuario_id>/',modificarUsuarioFuncionario,name='modificarUsuarioFuncionario'),
    path('eliminar_usuario/<int:usuario_id>/', eliminar_usuario, name='eliminar_usuario'),
    
    #Crud Instructor desde la vista de los funcionarios
    path('administrarInstructorFuncionario', administrarInstructorFuncionario, name='administrarInstructorFuncionario'),
    path('crearInstructorFuncionario',crearInstructorFuncionario,name='crearInstructorFuncionario'),
    path('modificarInstructorFuncionario',modificarInstructorFuncionario,name='modificarInstructorFuncionario'),
    
    #inscribir a taller vista desde el funcionario
    path('inscribir',inscribir,name='inscribir'),
    
    
    #mostrar Datos de Usuarios Logueado
    path('muestraDatosFuncionario',muestraDatosFuncionario,name='muestraDatosFuncionario'),
    path('muestraDatosUsuario',muestraDatosUsuario,name='muestraDatosUsuario'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
