from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .decorators import *
from .forms import FormularioRegistro
from .models import *

# Create your views here.
def inicio2(request):
    return render(request, 'inicio2.html', {"provincia": provincia})

def inicio(request):
    return render(request, 'inicio.html', {"provincia": provincia})


def basic_page(request):
    return render(request, 'basic_page.html')


def crear_ruta(request):
    if request.method == 'GET':
        return render(request, 'crear_ruta.html', {"tramo_horario": tramo_h, "tipo_rutas": tematica, "tipo_transporte": tipo_vehiculo, "Ciudad": Ciudad.objects.all().values()})
    else:
        nueva_ruta = Ruta()
        nueva_ruta.nombre = request.POST.get('nombre')
        nueva_ruta.tematica = request.POST.get('tipo_ruta')
        nueva_ruta.transporte = request.POST.get('tipo_transporte')
        nueva_ruta.tramo_horario = request.POST.get('tramo_horario')
        nueva_ruta.hora_inicio = request.POST.get('hora_inicio')
        nueva_ruta.hora_fin = request.POST.get('hora_fin')
        nueva_ruta.imagen = request.POST.get('imagen')
        nueva_ruta.operador_tur = request.POST.get(Operador_tur)
        Ruta.save(nueva_ruta)
        return render(request, 'inicio.html')


def mostrar_ruta(request):
    lista_rutas = Ruta.objects.all()
    return render(request, 'mostrar_ruta.html', {"rutas": lista_rutas})


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
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'inicio.html')
        else:
            return render(request, "registrar_usuario.html", {"form": form})


def registrar_operador(request):
    form = FormularioRegistro()
    if request.method == "GET":
        return render(request, "registrar_operador.html", {"form": form})
    #POST
    else:
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            user = UsuarioLogin()
            user.email = form.cleaned_data["email"]
            user.username = form.clean_username()
            user.password = make_password(request.POST.get("password2"))
            user.rol = Roles.OPERADOR
            user.save()
            return render(request, 'inicio.html')
        else:
            return render(request, "registrar_operador.html", {"form": form})


def login_usuario(request):
    form = AuthenticationForm()
    if request.method == "GET":
        return render(request, "login_usuario.html", {"form": form})
    elif request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)

    #Verificar que el formulario es valido
    if form.is_valid():
        #Intentar loguear
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],)

        #Si hemos encontrado el usuario
        if user is not None:
            #Nos logueamos
            login(request, user)
            return render(request, 'inicio.html', {"provincia" : provincia})


    else:
        #pasar errores a la vista
        for error in list(form.errors.values()):
            messages.error(request, error)
        return render(request, "login_usuario.html", {"form": form})


def login_operador(request):
    form = AuthenticationForm()

    if request.method == "GET":
        return render(request, "login_operador.html", {"form": form})
    elif request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)

        # Verificar que el formulario es valido
        if form.is_valid():
            # Intentar loguear
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'], )

            # Si hemos encontrado el usuario
            if user is not None:
                # Nos logueamos
                login(request, user)
                return render(request, 'inicio.html')

        else:
            # pasar errores a la vista
            for error in list(form.errors.values()):
                messages.error(request, error)
            return render(request, "login_operador.html", {"form": form})


@user_required
def desloguearse(request):
    logout(request)
    return render(request, "logout.html")
    #return redirect('/neas/logout/')
