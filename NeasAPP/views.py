from django.contrib.auth.hashers import make_password
from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from reportlab.pdfgen import canvas

from .decorators import *
from .forms import FormularioRegistro
from .forms import FormularioRegistroOPT
from .models import *

# Create your views here.
def inicio2(request):
    return render(request, 'inicio2.html', {"provincia": provincia})

def inicio(request):
    return render(request, 'inicio.html', {"provincia": provincia})

def forgot(request):
    return render(request, 'forgot.html')

def basic_page(request):
    return render(request, 'basic_page.html')

@operator_required
def crear_ruta(request):
    if request.method == 'GET':
        return render(request, 'crear_ruta.html', {"tramo_horario": tramo_h, "tipo_rutas": tematica, "tipo_transporte": tipo_vehiculo, "Provincia": provincia})
    else:
        nueva_ruta = Ruta()
        nueva_ruta.nombre = request.session['nombre']
        nueva_ruta.tematica = request.session['tipo_ruta']
        nueva_ruta.transporte = request.session['tipo_transporte']
        nueva_ruta.tramo_horario = request.session['tramo_horario']
        nueva_ruta.hora_inicio = request.session['hora_inicio']
        nueva_ruta.hora_fin = request.session['hora_fin']
        nueva_ruta.imagen = request.session['imagen']
        nueva_ruta.ciudad = request.session['ciudad']
        nueva_ruta.descripcion = request.session['desc']
        nueva_ruta.operador_tur_id = request.user.id
        nueva_ruta.precio = request.session['precio']
        Ruta.save(nueva_ruta)

        for m in request.POST.getlist('monumento'):

            nuevo_monumento_ruta = Monumento_Ruta()
            nuevo_monumento_ruta.Monumento = m
            nuevo_monumento_ruta.ruta = nueva_ruta
            nuevo_monumento_ruta.save()

        return inicio(request)

def modificar_ruta(request,id):

    ruta = Ruta.objects.get(id = id)

    if request.method == 'GET':
        return render(request, 'modificar_ruta.html',
                      {"ruta": ruta , "tramo_horario": tramo_h, "tipo_rutas": tematica, "tipo_transporte": tipo_vehiculo,
                       "provincia": provincia})
    else:
        ruta_act = ruta
        ruta_act.nombre = request.POST.get('nombre')
        ruta_act.tematica = request.POST.get('tipo_ruta')
        ruta_act.transporte = request.POST.get('tipo_transporte')
        ruta_act.tramo_horario = request.POST.get('tramo_horario')
        ruta_act.hora_inicio = request.POST.get('hora_inicio')
        ruta_act.hora_fin = request.POST.get('hora_fin')
        ruta_act.imagen = request.POST.get('imagen')
        ruta_act.ciudad = request.POST.get('ciudad')
        ruta_act.descripcion = request.POST.get('desc')
        ruta_act.operador_tur_id = request.user.id
        ruta_act.precio = request.POST.get('precio')
        Ruta.save(ruta_act)
        return mostrar_ruta(request)


def mostrar_ruta(request):
    lista_rutas = Ruta.objects.filter(operador_tur=request.user.id)
    return render(request, 'mostrar_ruta.html', {"rutas": lista_rutas, "tramo_horario": tramo_h, "tipo_rutas": tematica, "tipo_transporte": tipo_vehiculo})


def eliminar_ruta(request, id):
    ruta = Ruta.objects.get(id=id)
    Ruta.delete(ruta)
    return mostrar_ruta(request)


def registrar_usuario(request):
    form = FormularioRegistro()
    if request.method == "GET":
        return render(request, "registrar_usuario.html", {"form": form})
    #POST
    else:
        user = UsuarioLogin()
        form = FormularioRegistro(request.POST)
        user.email = form.data["email"]
        user.username = form.clean_username()
        user.password = make_password(request.POST.get("password2"))
        user.rol = Roles.CLIENTE
        user.save()
        return render(request, 'inicio.html')

#Registro Operador ANTIGUO (Handmade)
# def registrar_operador(request):
#     form = FormularioRegistro()
#     if request.method == "GET":
#         return render(request, "registrar_operador.html", {"form": form})
#     #POST
#     else:
#         form = FormularioRegistro(request.POST)
#         if form.is_valid():
#             user = OperadorLogin()
#             user.email = form.cleaned_data["email"]
#             user.username = form.clean_username()
#             user.password = make_password(request.POST.get("password2"))
#             user.rol = Roles.OPERADOR
#             user.save()
#             return render(request, 'inicio.html')
#         else:
#             return render(request, "registrar_operador.html", {"form": form})

def registrar_operador(request):
    if request.method == "GET":
        return render(request, "registrar_operador.html")
    #POST
    else:
        # form = formOPTHM(request.POST)
        form = AuthenticationForm(request=request, data=request.POST)
        # if form.is_valid():
        usuarioOP = UsuarioLogin()
        datosOP = DatosOperador()
        usuarioOP.username = form.data["username"]
        usuarioOP.password  =  make_password(request.POST.get("password2"))
        usuarioOP.rol = Roles.OPERADOR
        usuarioOP.email = form.data["email"]
        datosOP.cif = form.data["cif"]
        datosOP.telf = form.data["telf"]
        datosOP.a_fund = form.data["a_fund"]
        datosOP.website = form.data["website"]
        datosOP.forgot = form.data["forgot"]
        datosOP.info = form.data["info"]
        usuarioOP.save()
        datosOP.usuario = usuarioOP
        datosOP.save()

        return render(request, 'inicio.html')
        # else:
        #     return render(request, "registrar_operador.html", {"form": form})


def editar_perfil(request):

    user = request.user

    if request.method == 'GET':
        return render(request, 'editar_perfil.html',
                      {"usuario": user , "tramo_horario": tramo_h, "tipo_rutas": tematica, "tipo_transporte": tipo_vehiculo,
                       "provincia": provincia})
    else:
        usuario = user
        usuario.username = request.POST.get('username')
        usuario.email = request.POST.get('email')
        usuario.imagen = request.POST.get('imagen')
        UsuarioLogin.save(usuario)
        return inicio(request)


def cambiar_contraseña(request):

    usuario = UsuarioLogin.objects.get(username=request.session['usuario'])

    if request.method == 'GET':
        return render(request, 'cambiar_contraseña.html')
    else:
        user = usuario
        user.password = make_password(request.POST.get("password2"))
        UsuarioLogin.save(user)
        return inicio(request)


def login_usuario(request):
    form = AuthenticationForm()
    if request.method == "GET":
        return render(request, "login_usuario.html", {"form": form})
    elif request.method == "POST":
            form = AuthenticationForm(None, data=request.POST)

    #Verificar que el formulario es valido
    # if form.is_valid():
        #Intentar loguear
    user = authenticate(
        username=form.data['username'],
        password=form.data['password'],)

    request.session['usuario'] = form.data['username']

    #Si hemos encontrado el usuario
    if user is not None:
        #Nos logueamos
        login(request, user)
        return render(request, 'inicio.html', {"provincia": provincia})

    else:
        return render(request, 'error_loginOp.html')

def login_operador(request):
    form = AuthenticationForm()
    if request.method == "GET":
        return render(request, "login_operador.html", {"form": form})
    elif request.method == "POST":
        form = AuthenticationForm(None, data=request.POST)

    # Verificar que el formulario es valido
    # if form.is_valid():
    # Intentar loguear
    user = authenticate(
        username=form.data['username'],
        password=form.data['password'], )

    request.session['usuario'] = form.data['username']

    # Si hemos encontrado el usuario
    if user is not None:
        # Nos logueamos
        login(request, user)
        return render(request, 'inicio.html', {"provincia": provincia})

    else:
        return render(request, 'error_loginOp.html')


    # else:
    #     #pasar errores a la vista
    #     for error in list(form.errors.values()):
    #         messages.error(request, error)
    #     return render(request, "login_usuario.html", {"form": form})



#vamos a usar el loginusuario

# def login_operador(request):
#     form = AuthenticationForm()
#
#     if request.method == "GET":
#         return render(request, "login_operador.html", {"form": form})
#
#     elif request.method == "POST":
#         form = AuthenticationForm(request=request, data=request.POST)
#         # Verificar que el formulario es valido
#         if form.is_valid():
#             # Intentar loguear
#             user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'], )
#
#             # Si hemos encontrado el usuario
#             if user is not None and user.rol == "Operador":
#                 # Nos logueamos
#                 login(request, user)
#                 return render(request, 'inicio.html', {"provincia" : provincia})
#
#             else:
#                 return render(request, 'error_loginUser.html')
#
#         else:
#             # pasar errores a la vista
#             for error in list(form.errors.values()):
#                 messages.error(request, error)
#             return render(request, "login_operador.html", {"form": form})


@user_required
def desloguearse(request):
    logout(request)
    return render(request, "logout.html")
    #return redirect('/neas/logout/')

def buscar_ruta(request):
    ciudad = request.POST.get("provincia")
    list_rutas = Ruta.objects.filter(ciudad=ciudad)
    request.session['ciudad'] = ciudad
    return render(request, 'mostrar_ruta.html', {'rutas': list_rutas, "tramo_horario": tramo_h, "tipo_rutas": tematica, "tipo_transporte": tipo_vehiculo})

def filtro_general(request):
    transporte = request.POST.get("tipo_transporte")
    tramo_horario = request.POST.get("tramo_horario")
    tipo_ruta = request.POST.get("tipo_ruta")
    ciudad = request.session.get('ciudad')

    if transporte != None and tramo_horario != None and tipo_ruta != None:
        list_rutas = Ruta.objects.filter(ciudad=ciudad, transporte=transporte, tramo_horario=tramo_horario, tematica=tipo_ruta)

    elif transporte == None and tramo_horario != None and tipo_ruta != None:
        list_rutas = Ruta.objects.filter(ciudad=ciudad, tramo_horario=tramo_horario, tematica=tipo_ruta)

    elif tramo_horario == None and tipo_ruta != None and transporte != None:
        list_rutas = Ruta.objects.filter(ciudad=ciudad, transporte=transporte, tematica=tipo_ruta)

    elif tipo_ruta == None and tramo_horario != None and transporte != None:
        list_rutas = Ruta.objects.filter(ciudad=ciudad, transporte=transporte, tramo_horario=tramo_horario)

    elif transporte == None and tramo_horario == None and tipo_ruta != None:
        list_rutas = Ruta.objects.filter(ciudad=ciudad, tematica=tipo_ruta)

    elif transporte == None and tipo_ruta == None and tramo_horario != None:
        list_rutas = Ruta.objects.filter(ciudad=ciudad, tramo_horario=tramo_horario)

    elif transporte == None and tramo_horario == None and tipo_ruta == None:
        list_rutas = Ruta.objects

    else:
        list_rutas = Ruta.objects.filter(ciudad=ciudad, transporte=transporte)

    return render(request, 'mostrar_ruta.html', {'rutas': list_rutas, "tramo_horario": tramo_h, "tipo_rutas": tematica, "tipo_transporte": tipo_vehiculo})


def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')

def terminos(request):
    return render(request, 'terminos.html')

def politicas(request):
    return render(request, 'politicas.html')

def centroAyuda(request):
    return render(request, 'centro_ayuda.html')

@operador_required
def vista_operador(request):
    # Código de la vista para usuarios con rol de operador
    return render(request, 'pagina_operador.html')

def acceso_denegado(request):
    return render(request, 'acceso_denegado.html')


def eleccion_operador(request):
    # Código de la vista para usuarios con rol de operador
    if request.POST['menu'] == 'crear':
        return render(request, 'crear_ruta.html')
    else:
        return redirect(mostrar_ruta)


def eleccion_monumento(request):

    request.session['nombre'] = request.POST.get('nombre')
    request.session['tipo_ruta'] = request.POST.get('tipo_ruta')
    request.session['tipo_transporte'] = request.POST.get('tipo_transporte')
    request.session['tramo_horario'] = request.POST.get('tramo_horario')
    request.session['hora_inicio'] = request.POST.get('hora_inicio')
    request.session['hora_fin'] = request.POST.get('hora_fin')
    request.session['imagen'] = request.POST.get('imagen')
    request.session['ciudad'] = request.POST.get('ciudad')
    request.session['desc'] = request.POST.get('desc')
    request.session['precio'] = request.POST.get('precio')

    return render(request, 'eleccion_monumento.html', {'monumentos': Monumentos})


def rutas_mas_valoradas(request):
    rutas = Ruta.objects.annotate.order_by('valoracion_media')[:5]
    return render(request, 'rutas_mas_valoradas.html', {'rutas': rutas})


def generar_pdf(request):
    rutas = request.POST.getlist('rutas')
    # Obtener los datos de las rutas seleccionadas
    # routes = ...

    # Crear el objeto HttpResponse con el tipo de contenido PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="rutas.pdf"'

    # Crear el objeto PDF utilizando ReportLab
    p = canvas.Canvas(response)

    # Agregar contenido al PDF
    p.setFont("Helvetica", 12)
    p.drawString(100, 700, "Rutas seleccionadas:")

    y = 670
    for r in rutas:
        p.drawString(100, y, r.nombre)
        y -= 20

    # Finalizar el PDF
    p.showPage()
    p.save()

    return response
