from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.db.models import Model, ForeignKey

# Create your models here.

#Creamos los Enum para los valores de BBDD
class tipo_vehiculo(models.TextChoices):

    turismo = ('Turismo')
    ciclomotor = ('Ciclomotor')
    motocicleta = ('Motocicleta')
    bici = ('Bicicleta')
    caminando = ('A pie')


class tematica(models.TextChoices):

    gastronomico = ('Gastronómico')
    cultural = ('Cultural')
    historico = ('Historico')
    ocio = ('Ocio')
    naturaleza = ('Naturaleza')
    religioso = ('Religioso')


class tramo_h(models.TextChoices):
    mañana = ('Mañana')
    tarde = ('Tarde')
    noche = ('Noche')

class provincia(models.TextChoices):

    sevilla = 'SEV', ('Sevilla')
    cadiz = 'CDZ', ('Cádiz')
    granada = 'GRA', ('Granada')
    cordoba = 'COR', ('Cordoba')
    huelva = 'HLV', ('Huelva')
    jaen = 'JN', ('Jaen')
    almeria = 'ALM', ('Almeria')
    malaga = 'MAL', ('Malaga')
    caceres = 'CAC', ('Caceres')
    badajoz = 'BAD', ('Badajoz')
    murcia = 'MUR', ('Murcia')
    alicante = 'ALI', ('Alicante')
    valencia = 'VAL', ('Valencia')
    castellon = 'CAST', ('Castellon')
    islas_baleares = 'ISBL', ('Islas Baleares')
    tenerife = 'TNF', ('Tenerife')
    las_palmas = 'LAPM', ('las Palmas')
    albacete = 'ALB', ('Albacete')
    cuenca = 'CUEN', ('cuenca')
    toledo = 'TOL', ('Toledo')
    ciudad_real = 'CDRL', ('Ciudad Real')
    guadalajara = 'GUAL', ('Guadalajara')
    madrid = 'MADR', ('Madrid')
    teruel = 'TER', ('Teruel')
    zaragoza = 'ZAR', ('Zaragoza')
    huesca = 'H',('Huesca')
    tarragona = 'TARR', ('Tarragona')
    lerida = 'LER', ('lerida')
    barcelona = 'BAR',('Barcelona')
    gerona = 'GER', ('Gerona')
    la_rioja = 'LARJ', ('La Rioja')
    navarra = 'NAV', ('Navarra')
    vizcaya = 'VZY', ('Vizcaya')
    alava = 'ALA', ('Alava')
    cantabria = 'CANT', ('Cantabria')
    asturias = 'AST', ('Asturias')
    lugo = 'LGO',('Lugo')
    orense = 'ORS',('Orense')
    pontevedra = 'PNVD',('Pontevedra')
    la_coruña = 'LCÑA',('La Coruña')
    leon = 'LN',('León')
    palencia = 'PL', ('Palencia')
    burgos = 'BRG',('burgos')
    soria = 'SOR', ('Soria')
    valladolid = 'VLLD',('Valladolid')
    segovia = 'SEG',('Segovia')
    avila = 'AVLA',('Avila')
    salamanca = 'SAL',('Salamanca')
    zamora = 'ZAM',('Zamora')



"""CREACIÓN DE LA BASE DE DATOS"""
#Entidades de la base de datos

class Usuario(models.Model):
    nombre = models.CharField(max_length=150)
    Apellidos = models.CharField(max_length=150)
    dni = models.CharField(max_length=9)
    email = models.EmailField(max_length=150)

class Operador_tur(models.Model):
    nombre = models.CharField(max_length=100)
    cif = models.CharField(max_length=9)
    email = models.CharField(max_length=150)
    fecha_fundacion_oper = models.DateField()
    logo = models.CharField(max_length=500)
    telefono = models.CharField(max_length=50)
    sitio_web = models.CharField(max_length=500)

class Ruta(models.Model):
    nombre = models.CharField(max_length=500, default=None)
    hora_inicio = models.TimeField(default=None)
    hora_fin = models.TimeField(default=None)
    tematica = models.CharField(choices=tematica.choices, max_length=100)
    tramo_horario = models.CharField(max_length=50, choices=tramo_h.choices)
    transporte = models.CharField(choices=tipo_vehiculo.choices, max_length=100)
    valoracion_media = models.FloatField(max_length=4, default=0.0)
    operador_tur = models.ForeignKey(Operador_tur, on_delete=models.CASCADE, default=None, null=True)
    usuarios = models.ManyToManyField(Usuario, default=None)

class Ciudad(models.Model):
    nombre = models.CharField(choices=provincia.choices, max_length=100)
    es_capital = models.BooleanField(default=False)
    rutas = models.ManyToManyField(Ruta)

class Valoracion_usuario(models.Model):
    num_estrellas = models.IntegerField()
    rutas = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    usuarios = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Monumento_pi(models.Model):
    nombre = models.CharField(max_length=150)
    imagen = models.CharField(max_length=500)
    horario_visita = models.TimeField()
    latitud = models.PositiveIntegerField()
    longitude = models.PositiveIntegerField()
    ciudades = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    rutas = models.ManyToManyField(Ruta)
    valoraciones = models.ManyToManyField(Valoracion_usuario)

class Roles(models.TextChoices):
    ADMIN = 'Admin'
    CLIENTE = 'Cliente'
    OPERADOR = 'Operador'

    def mostrar(self):
        return

class UsuarioLogin(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, unique=True)
    rol = models.CharField(max_length=100, choices=Roles.choices, default=Roles.CLIENTE, null=True)
    USERNAME_FIELD = 'username'

class UsuarioManager(BaseUserManager):

    def create_user(self, email, ):
        return