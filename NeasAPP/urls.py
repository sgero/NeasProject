from django.urls import path, include
from .views import *

urlpatterns = [
    path('inicio', inicio),
    path('ruta/crear/', crear_ruta),
    path('ruta/', mostrar_rutas),
    path('login', registrar_usuario),
    path('registrar/', registrar_usuario),
    # path('logout', ),
    # path('register', ),
]