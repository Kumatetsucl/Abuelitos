from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('registro',registro,name='registro'),
    path('login',login,name='login'),
    path('LogueadoTalleresUsuario',LogueadoTalleresUsuario,name='LogueadoTalleresUsuario'),
    path('InscripcionTalleresUsuario',InscripcionTalleresUsuario,name='InscripcionTalleresUsuario')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
