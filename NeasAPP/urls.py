from django.urls import path, include
from .views import *

urlpatterns = [
    path('', inicio),
    path('ruta/crear/', crear_ruta),
    path('ruta/', mostrar_rutas)
]