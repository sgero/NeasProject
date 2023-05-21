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

class Monumentos(models.TextChoices):
    LaSagradaFamilia = ('La Sagrada Familia')
    LaAlhambra = ('La Alhambra')
    LaCatedralDeSantiagoDeCompostela = ('La Catedral de Santiago de Compostela')
    LaMezquitaCatedralDeCórdoba = ('La Mezquita-Catedral de Córdoba')
    ElPalacioRealDeMadrid = ('El Palacio Real de Madrid')
    LaGiralda = ('La Giralda')
    ElParqueGüell = ('El Parque Güell')
    LaTorreDelOro = ('La Torre del Oro')
    ElAcueductoDeSegovia = ('El Acueducto de Segovia')
    LaPlazaDeEspaña = ('La Plaza de España')
    LaCiudadDeLasArtesYLasCienciasDeValencia = ('La Ciudad de las Artes y las Ciencias de Valencia')
    ElParqueNacionalDeDoñana = ('El Parque Nacional de Doñana')
    ElTeatroRomanoDeMérida = ('El Teatro Romano de Mérida')
    LaBasílicaDelPilarEnZaragoza = ('La Basílica del Pilar en Zaragoza')
    LaTorreDeHérculesEnLaCoruña = ('La Torre de Hércules en La Coruña')
    ElMuseoDelPradoEnMadrid = ('El Museo del Prado en Madrid')
    LaCatedralDeBurgos = ('La Catedral de Burgos')
    LaCiudadEncantadaEnCuenca = ('La Ciudad Encantada en Cuenca')
    LaMurallaRomanaDeLugo = ('La Muralla Romana de Lugo')
    LaAlcazabaDeMálaga = ('La Alcazaba de Málaga')
    LaTorreDelOroEnSevilla = ('La Torre del Oro en Sevilla')
    ElCastilloDeLoarreEnHuesca = ('El Castillo de Loarre en Huesca')
    ElMonasterioDeSanLorenzoDeElEscorialEnMadrid = ('El Monasterio de San Lorenzo de El Escorial en Madrid')
    ElPuenteNuevoDeRondaEnMálaga = ('El Puente Nuevo de Ronda en Málaga')
    LaPlayaDeLaConchaEnSanSebastián = ('La Playa de la Concha en San Sebastián')
    ElMonasterioDePobletEnTarragona = ('El Monasterio de Poblet en Tarragona')
    ElPalacioDeLaAlhóndigaEnZamora = ('El Palacio de la Alhóndiga en Zamora')
    LaBasílicaDeLaSagradaFamiliaEnBarcelona = ('La Basílica de la Sagrada Familia en Barcelona')
    LaCuevaDeAltamiraEnCantabria = ('La Cueva de Altamira en Cantabria')
    LaCasaBatllóEnBarcelona = ('La Casa Batlló en Barcelona')
    ElParqueDeMaríaLuisaEnSevilla = ('El Parque de María Luisa en Sevilla')
    LaTorreDeLaVelaEnGranada = ('La Torre de la Vela en Granada')
    ElAcueductoDeLosMilagrosEnMérida = ('El Acueducto de los Milagros en Mérida')
    LaBasílicaDeSantaMaríaDelMarEnBarcelona = ('La Basílica de Santa María del Mar en Barcelona')
    ElParqueNaturalDeLasIslasCíesEnGalicia = ('El Parque Natural de las Islas Cíes en Galicia')
    LaCatedralDeSevilla = ('La Catedral de Sevilla')
    ElParqueDelRetiroEnMadrid = ('El Parque del Retiro en Madrid')
    ElPalacioDeLaMagdalenaEnSantander = ('El Palacio de la Magdalena en Santander')
    LaIglesiaDeSanFranciscoElGrandeEnMadrid = ('La Iglesia de San Francisco el Grande en Madrid')
    ElMonasterioDeSanJuanDeLaPeñaEnHuesca = ('El Monasterio de San Juan de la Peña en Huesca')
    LaPlayaDeLasCatedralesEnLugo = ('La Playa de las Catedrales en Lugo')
    LaPlazaMayorDeSalamanca = ('La Plaza Mayor de Salamanca')
    ElParqueDeLaNaturalezaDeCabárcenoEnCantabria = ('El Parque de la Naturaleza de Cabárceno en Cantabria')
    LaTorreDeLaMalmuertaEnCórdoba = ('La Torre de la Malmuerta en Córdoba')
    ElRealAlcázarDeSevilla = ('El Real Alcázar de Sevilla')
    LaPlayaDeBoloniaEnCádiz = ('La Playa de Bolonia en Cádiz')
    ElPalacioDeLaGeneralitatDeValencia = ('El Palacio de la Generalitat de Valencia')
    LaCatedralDeLeón = ('La Catedral de León')
    ElMonasterioDeMontserratEnBarcelona = ('El Monasterio de Montserrat en Barcelona')
    ElMuseoGuggenheimEnBilbao = ('El Museo Guggenheim en Bilbao')



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
    rol = models.CharField(max_length=100, choices=Roles.choices, default=Roles.CLIENTE, null=True, unique=None)
    imagen = models.CharField(max_length=1000, null=True, unique=True, default='NeasAPP/static/img/userfoto.png')
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username, email, password']

    objects = UsuarioManager()

    def __str__(self):
        return self.username, self.email

class DatosUsuario(models.Model):
    dni = models.CharField(max_length=9, null=True)
    usuario = models.ForeignKey(UsuarioLogin, on_delete=models.CASCADE, default=None, null=True)

  #Clase para el formulario de registro de Operador Turístico (Creo que esto no hace falta ya que tenemos el UsuarioLogin, pero lo creo por si acaso)
class DatosOperador(models.Model):
    # email = models.EmailField(unique=True)
    # username = models.CharField(max_length=50, unique=True)
    # password = models.CharField(max_length=50, unique=True)
    # rol = models.CharField(max_length=100, choices=Roles.choices, default=Roles.OPERADOR, null=True, unique=None)
    cif = models.CharField(max_length=255, null=True)
    telf = models.CharField(max_length=255, null=True)
    a_fund = models.CharField(max_length=4, null=True)
    website = models.CharField(max_length=1000, null=True)
    logo = models.CharField(max_length=1000, null=True)
    forgot = models.CharField(max_length=50, null=True)
    info = models.CharField(max_length=1000, null=True)
    usuario = models.ForeignKey(UsuarioLogin, on_delete=models.CASCADE, default=None, null=True)

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username, email, password, cif, telf, a_fund, website, logo, forgot, info']
    #
    # objects = UsuarioManager()
    #
    # def __str__(self):
    #     return self.username, self.email


#Entidades de la base de datos
#ESTA CLASE NO HEREDA DEL LOGIN DE DJANGO (ABSTRACTBASE USER SI, QUE ES LA QUE VAMOS A USAR)
# class Usuario(models.Model):
#     nombre = models.CharField(max_length=150)
#     Apellidos = models.CharField(max_length=150)
#     dni = models.CharField(max_length=9)
#     email = models.EmailField(max_length=150)
#     forgot = models.CharField(max_length=50)
#     usuario_login = models.ForeignKey(UsuarioLogin, on_delete=models.CASCADE, default=None)


# class Operador_tur(models.Model):
#     nombre = models.CharField(max_length=100)
#     cif = models.CharField(max_length=9)
#     email = models.CharField(max_length=150)
#     fecha_fundacion_oper = models.DateField()
#     logo = models.CharField(max_length=500)
#     info = models.CharField(max_length=1000)
#     telf = models.CharField(max_length=50)
#     sitio_web = models.CharField(max_length=500)
#     forgot = models.CharField(max_length=50)
#     usuario_login = models.ForeignKey(UsuarioLogin, on_delete=models.CASCADE, default=None)

class Ciudad(models.Model):
    nombre = models.CharField(choices=provincia.choices, max_length=100)
    es_capital = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


class Ruta(models.Model):
    nombre = models.CharField(max_length=500, default=None)
    hora_inicio = models.TimeField(default=None)
    hora_fin = models.TimeField(default=None)
    tematica = models.CharField(choices=tematica.choices, max_length=100)
    tramo_horario = models.CharField(max_length=50, choices=tramo_h.choices)
    transporte = models.CharField(choices=tipo_vehiculo.choices, max_length=100)
    imagen = models.ImageField(default=None)
    valoracion_media = models.FloatField(max_length=4, default=0.0)
    operador_tur = models.ForeignKey(UsuarioLogin, on_delete=models.CASCADE, default=None, null=True)
    ciudad = models.CharField(choices=provincia.choices, max_length=200, null=True)
    descripcion = models.CharField(max_length=50, default='Descripción', null=True)
    precio = models.FloatField(null=True)


# class DatosMonumentos(models.Model):
#     monumento = models.CharField(max_length=60, choices=Monumentos.choices, null=True)
#     imagen = models.URLField(null=True)
#     ciudad = models.CharField(max_length=60, choices=provincia.choices, null=True)
#     valoracion_media = models.FloatField(max_length=4, default=0.0, null=True)
#     valoracion_usuario = models.ForeignKey(Valoracion_usuario, on_delete=models.CASCADE, null=True)
#     ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, null=True)

class Valoracion_usuario(models.Model):
    nota = models.FloatField(null=True)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, default=None, null=True)
    usuarios = models.ForeignKey(UsuarioLogin, on_delete=models.CASCADE, null=True)
    comentario = models.CharField(max_length=200, null=True)

class Monumento_pi(models.Model):
    nombre = models.CharField(max_length=150, choices=Monumentos.choices)
    imagen = models.CharField(max_length=500)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, null=True)
    valoracion_media = models.FloatField(max_length=4, default=0.0, null=True)
    valoracion_usuario = models.ForeignKey(Valoracion_usuario, on_delete=models.CASCADE, null=True)

class Monumento_Ruta(models.Model):
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, null=True)
    Monumento = models.CharField(choices=Monumentos.choices, max_length=200, null=True)
