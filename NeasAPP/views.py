from django.shortcuts import render
from .models import *

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')


def crear_ruta(request):

    if request.method == 'GET':
        return render(request, 'crear_ruta.html', {"tramo_horario": tramo_h, "tipo_rutas": tematica, "tipo_transporte": tipo_vehiculo})
    else:
        nueva_ruta = Ruta()
        nueva_ruta.nombre = request.POST.get('nombre')
        nueva_ruta.tipo_ruta = request.POST.get('tipo_ruta')
        nueva_ruta.tipo_transporte = request.POST.get('tipo_transporte')
        nueva_ruta.tramo_horario = request.POST.get('tramo_horario')
        nueva_ruta.hora_inicio = request.POST.get('hora_inicio')
        nueva_ruta.hora_fin = request.POST.get('hora_fin')
        Ruta.save(nueva_ruta)
        return render(request, 'inicio.html')


def mostrar_ruta(request):

    lista_rutas = Ruta.objects.all()
    return render(request, 'mostrar_ruta.html', {"rutas": lista_rutas})

def registrar_usuario(request):

    if request.method == 'GET':
        form = FormularioRegistro()
        return render(request, 'registrar.html')
    else:
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            form.save()
            Username = form.cleaned_data.get('Username')
            Contraseña = form.cleaned_data.get('Contraseña')
            User = authenticate(Username=Username, Contraseña=Contraseña)
            return render(request, 'inicio.html')