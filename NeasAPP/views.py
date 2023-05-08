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


def basic_page(request):
    return render(request, 'basic_page.html')


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
        nueva_ruta.operador_tur = request.POST.get(Operador_tur)
        nueva_ruta.ciudad = request.POST.get('ciudad')
        nueva_ruta.descripcion = request.POST.get('desc')
        Ruta.save(nueva_ruta)
        return render(request, 'inicio.html')


def mostrar_ruta(request):
    lista_rutas = Ruta.objects.all()
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
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'inicio.html')
        else:
            return render(request, "registrar_usuario.html", {"form": form})

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
    form = FormularioRegistroOPT()
    if request.method == "GET":
        return render(request, "registrar_operador.html", {"form": form})
    #POST
    else:
        form = FormularioRegistroOPT(request.POST)
        if form.is_valid():
            form.save()
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

def buscar_ruta(request):
    ciudad = request.POST.get("provincia")
    list_rutas = Ruta.objects.filter(ciudad=ciudad)
    return render(request, 'mostrar_ruta.html', {'rutas': list_rutas, "tramo_horario": tramo_h, "tipo_rutas": tematica, "tipo_transporte": tipo_vehiculo})

def filtro_general(request, ciudad):
    transporte = request.POST.get("tipo_transporte")
    tramo_horario = request.POST.get("tramo_horario")
    tipo_ruta = request.POST.get("tipo_ruta")
    if ciudad == ciudad:
        if transporte != None and tramo_horario != None and tipo_ruta != None:
            list_rutas = Ruta.objects.filter(transporte=transporte, tramo_horario=tramo_horario, tematica=tipo_ruta)

        elif transporte == None and tramo_horario != None and tipo_ruta != None:
            list_rutas = Ruta.objects.filter(tramo_horario=tramo_horario, tematica=tipo_ruta)

        elif tramo_horario == None and tipo_ruta != None and transporte != None:
            list_rutas = Ruta.objects.filter(transporte=transporte, tematica=tipo_ruta)

        elif tipo_ruta == None and tramo_horario != None and transporte != None:
            list_rutas = Ruta.objects.filter(transporte=transporte, tramo_horario=tramo_horario)

        elif transporte == None and tramo_horario == None and tipo_ruta != None:
            list_rutas = Ruta.objects.filter(tematica=tipo_ruta)

        elif transporte == None and tipo_ruta == None and tramo_horario != None:
            list_rutas = Ruta.objects.filter(tramo_horario=tramo_horario)

        elif transporte == None and tramo_horario == None and tipo_ruta == None:
            list_rutas = Ruta.objects

        else:
            list_rutas = Ruta.objects.filter(transporte=transporte)

    return render(request, 'mostrar_ruta.html', {'rutas': list_rutas, "tramo_horario": tramo_h, "tipo_rutas": tematica, "tipo_transporte": tipo_vehiculo})


def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')