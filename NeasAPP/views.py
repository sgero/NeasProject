from django.shortcuts import render
from .models import *

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')


def crear_ruta(request):

    if request.method == 'GET':
        return render(request, 'crear_ruta.html', {"tipo_rutas": tipo, "tipo_transporte": tipo_vehiculo})
    else:
        nueva_ruta = recorrido()
        nueva_ruta.nombre = request.POST.get('nombre')
        nueva_ruta.tipo_ruta = request.POST.get('tipo_ruta')
        nueva_ruta.tipo_transporte = request.POST.get('tipo_transporte')
        nueva_ruta.total_tiempo = int(request.POST.get('total_tiempo'))
        recorrido.save(nueva_ruta)
        return render(request, 'inicio.html')


def mostrar_rutas(request):

    lista_rutas = recorrido.objects.all()
    return render(request, 'mostrar_rutas.html', {"rutas": lista_rutas})