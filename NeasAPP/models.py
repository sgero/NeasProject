from django.db import models
from django.db.models import Model, ForeignKey
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

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

    sevilla =('Sevilla')
    cadiz = ('Cádiz')
    granada = ('Granada')
    cordoba = ('Cordoba')
    huelva = ('Huelva')
    jaen = ('Jaen')
    almeria = ('Almeria')
    malaga = ('Malaga')
    caceres = ('Caceres')
    badajoz = ('Badajoz')
    murcia = ('Murcia')
    alicante =('Alicante')
    valencia = ('Valencia')
    castellon =  ('Castellon')
    islas_baleares = ('Islas Baleares')
    tenerife =  ('Tenerife')
    las_palmas =  ('Las Palmas')
    albacete = ('Albacete')
    cuenca =  ('Cuenca')
    toledo =  ('Toledo')
    ciudad_real =  ('Ciudad Real')
    guadalajara =('Guadalajara')
    madrid =  ('Madrid')
    teruel = ('Teruel')
    zaragoza =  ('Zaragoza')
    huesca =('Huesca')
    tarragona = ('Tarragona')
    lerida =  ('Lerida')
    barcelona = ('Barcelona')
    gerona =  ('Gerona')
    la_rioja =  ('La Rioja')
    navarra =  ('Navarra')
    vizcaya = ('Vizcaya')
    alava =  ('Alava')
    cantabria = ('Cantabria')
    asturias = ('Asturias')
    lugo = ('Lugo')
    orense = ('Orense')
    pontevedra =('Pontevedra')
    la_coruña = ('La Coruña')
    leon = ('León')
    palencia = ('Palencia')
    burgos = ('Burgos')
    soria =  ('Soria')
    valladolid = ('Valladolid')
    segovia = ('Segovia')
    avila = ('Avila')
    salamanca = ('Salamanca')
    zamora = ('Zamora')



"""CREACIÓN DE LA BASE DE DATOS"""
#Entidades para el login y los roles
class Roles(models.TextChoices):
    ADMIN = 'Admin'
    CLIENTE = 'Cliente'
    OPERADOR = 'Operador'

    def mostrar(self):
        return

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un email válido")
        user = self.model(email=self.normalize_email(email),**extra_fields )
        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_superuser(self,email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault("is_susperuser", True)
        return self.create_user(email,password,**extra_fields)

class UsuarioLogin(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, unique=True)
    rol = models.CharField(max_length=100, choices=Roles.choices, default=Roles.CLIENTE, null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username, email, password']

    objects = UsuarioManager()

    def __str__(self):
        return self.username, self.email


#Entidades de la base de datos
class Usuario(models.Model):
    nombre = models.CharField(max_length=150)
    Apellidos = models.CharField(max_length=150)
    dni = models.CharField(max_length=9)
    email = models.EmailField(max_length=150)
    usuario_login = models.ForeignKey(UsuarioLogin, on_delete=models.CASCADE, default=None)


class Operador_tur(models.Model):
    nombre = models.CharField(max_length=100)
    cif = models.CharField(max_length=9)
    email = models.CharField(max_length=150)
    fecha_fundacion_oper = models.DateField()
    logo = models.CharField(max_length=500)
    telefono = models.CharField(max_length=50)
    sitio_web = models.CharField(max_length=500)
    usuario_login = models.ForeignKey(UsuarioLogin, on_delete=models.CASCADE, default=None)

class Ruta(models.Model):
    nombre = models.CharField(max_length=500, default=None)
    hora_inicio = models.TimeField(default=None)
    hora_fin = models.TimeField(default=None)
    tematica = models.CharField(choices=tematica.choices, max_length=100)
    tramo_horario = models.CharField(max_length=50, choices=tramo_h.choices)
    transporte = models.CharField(choices=tipo_vehiculo.choices, max_length=100)
    imagen = models.CharField(max_length=500, default=None)
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

