from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
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
        nueva_ruta.nombre = request.POST.get('nombre')
        nueva_ruta.tematica = request.POST.get('tipo_ruta')
        nueva_ruta.transporte = request.POST.get('tipo_transporte')
        nueva_ruta.tramo_horario = request.POST.get('tramo_horario')
        nueva_ruta.hora_inicio = request.POST.get('hora_inicio')
        nueva_ruta.hora_fin = request.POST.get('hora_fin')
        nueva_ruta.imagen = request.POST.get('imagen')
        nueva_ruta.ciudad = request.POST.get('ciudad')
        nueva_ruta.descripcion = request.POST.get('desc')
        nueva_ruta.operador_tur_id = request.user.id
        nueva_ruta.precio = request.POST.get('precio')
        Ruta.save(nueva_ruta)
        return render(request, 'inicio.html', {"provincia":provincia})


def mostrar_ruta(request):
    lista_rutas = Ruta.objects.filter(operador_tur=request.user.id)
    return render(request, 'mostrar_ruta.html', {"rutas": lista_rutas, "tramo_horario": tramo_h, "tipo_rutas": tematica, "tipo_transporte": tipo_vehiculo})


def eliminar_ruta(request, id):
    ruta = Ruta.objects.get(id=id)
    Ruta.delete(ruta)
    return redirect('/neas/ruta')


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

    #Si hemos encontrado el usuario
    if user is not None:
        #Nos logueamos
        login(request, user)
        if user.rol == "Operador":

            return render(request, 'pagina_operador.html', {"provincia": provincia})

        else:
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
