from django.urls import path, include

from . import views
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('inicio2/', inicio2, name='inicio2'),
    path('buscar/', buscar_ruta, name='buscar_ruta'),
    path('buscar/<str:ciudad>/', buscar_ruta, name='buscar_ruta_ciudad'),
    path('buscar/personalizada/', filtro_general, name='filtro'),
    path('ruta/crear/', crear_ruta, name='crear_ruta'),
    path('ruta/', mostrar_ruta, name='mostrar_ruta'),
    path('login/usuario', login_usuario, name='login_usuario'),
    # path('login/operador', login_operador, name='login_operador'),
    path('registrar/usuario/', registrar_usuario, name='registrar_usuario'),
    path('registrar/operador/', registrar_operador, name='registrar_operador'),
    path('basic/page/', basic_page),
    path('logout/', desloguearse, name='logout'),
    path('ruta/eliminar/<int:id>', eliminar_ruta, name='eliminar_ruta'),
    path('ruta/valorar/<int:id>', valorar_ruta, name='valorar_ruta'),
    path('aboutUs/', sobre_nosotros, name='sobre_nosotros'),
    path('terminos&condiciones/', terminos, name='terminos&condiciones'),
    path('politicaPrivacidad/', politicas, name='politicaPrivacidad'),
    path('centroAyuda/', centroAyuda, name='centroAyuda'),
    path('ruta/<int:ruta_id>/', mostrar_ruta, name='mostrar_ruta'),
    path('ruta/<int:ruta_id>/valorar/', valorar_ruta, name='valorar_ruta'),
]
