from django.urls import path, include
from .views import *

urlpatterns = [
    path('', inicio),
    path('ruta/crear/', crear_ruta),
    path('ruta/', mostrar_ruta),
    path('login/usuario', login_usuario, name='login_usuario'),
    path('login/operador', login_operador, name='login_operador'),
    path('registrar/usuario/', registrar_usuario),
    path('registrar/operador/', registrar_operador),
    # path('logout', ),
    # path('register', ),
]