from django.urls import path, include
from .views import *

urlpatterns = [
    path('', inicio),
    path('ruta/crear/', crear_ruta),
    path('ruta/', mostrar_ruta),
    path('login/', registrar_usuario),
    path('registrar/usuario/', registrar_usuario),
    path('registrar/operador/', registrar_operador),
    path('basic/page/', basic_page),
    # path('logout', ),
    # path('register', ),
]