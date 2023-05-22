from django.urls import path, include
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('inicio2/', inicio2, name='inicio2'),
    path('buscar/<str:ciudad>', buscar_ruta, name='buscar_ruta_ciudad'),
    path('buscar/', buscar, name='buscar'),
    path('buscar/personalizada/', filtro_general, name='filtro'),
    path('ruta/crear/', crear_ruta, name='crear_ruta'),
    path('ruta/modificar/<int:id>', modificar_ruta, name='modificar_ruta'),
    path('ruta/<int:ruta_id>/', mostrar_ruta, name='mostrar_ruta'),
    path('ruta/', mostrar_ruta_op, name='mostrar_ruta_op'),
    #path('ruta/<int:id>', mostrar_ruta_especifica, name='mostrar_ruta_especifica'),
    path('login/usuario', login_usuario, name='login_usuario'),
    #path('login/operador', login_operador, name='login_operador'),
    path('registrar/usuario/', registrar_usuario, name='registrar_usuario'),
    path('registrar/operador/', registrar_operador, name='registrar_operador'),
    path('cambiar/contraseña/', cambiar_contraseña, name='cambiar_contraseña'),
    path('editar/', editar_perfil, name='editar_perfil'),
    path('basic/page/', basic_page),
    path('logout/', desloguearse, name='logout'),
    path('ruta/eliminar/<int:id>', eliminar_ruta, name='eliminar_ruta'),
    path('aboutUs/', sobre_nosotros, name='sobre_nosotros'),
    path('terminos&condiciones/', terminos, name='terminos&condiciones'),
    path('politicaPrivacidad/', politicas, name='politicaPrivacidad'),
    path('centroAyuda/', centroAyuda, name='centroAyuda'),
    path('accesoDenegados/', acceso_denegado, name='acceso_denegado'),
    path('eleccionOperador/', eleccion_operador, name='eleccion_operador'),
    path('eleccionMonumento/', eleccion_monumento, name='eleccion_monumento'),
    # path('paginaOperador/', vista_operador, name='vista_operador'),
    path('rutas_mas_valoradas/', rutas_mas_valoradas, name='rutas_mas_valoradas'),
    path('generar_pdf/', generar_pdf, name='generar_pdf'),
    path('ruta/valorar/<int:id>', valorar_ruta, name='valorar_ruta'),
    path('ruta/<int:ruta_id>/valorar/', valorar_ruta, name='valorar_ruta2'),
    path('ruta/detalles/<int:id>', DetallesRutas, name='detalles_ruta'),
    path('rutas/', mostrar_todas_rutas, name='mostrar_todas_rutas'),

    # path('paginaOperador/', vista_operador, name='vista_operador')

]
