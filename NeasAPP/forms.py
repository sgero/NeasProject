from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import UsuarioLogin


class FormularioRegistro(UserCreationForm):

    email = forms.EmailField(max_length=255, required=True,
                             help_text='Requerido. Ingrese una dirección de correo electrónico válida.')

    username = forms.CharField(max_length=255, required=True,
                               help_text='Requerido. 255 caracteres o menos. Solo letras, números y @/./+/-/_ caracteres.')

    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    forgot = forms.CharField(max_length=50, required=True,
                             help_text='Requerido. Introduce una pista para recordar tu contraseña')
    class Meta:
        model = UsuarioLogin
        fields = ('email', 'username', 'password1', 'password2')



#Formulario de registro para Operadores Turísticos
class FormularioRegistroOPT(UserCreationForm):

    email = forms.EmailField(max_length=255, required=True,
                             help_text='Requerido. Ingrese una dirección de correo electrónico válida.')

    username = forms.CharField(max_length=255, required=True,
                               help_text='Requerido. 255 caracteres o menos. Solo letras, números y @/./+/-/_ caracteres.')

    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    cif = forms.CharField(max_length=255, required=False,
                          help_text='Requerido. 9 caracteres')

    telf = forms.CharField(max_length=255, required=False,
                          help_text='Requerido.')

    a_fund = forms.IntegerField(required=False,
                          help_text='Requerido.')

    website = forms.URLField(max_length=1000, required=False,
                          help_text='Requerido.')

    logo = forms.URLField(max_length=1000, required=False,
                          help_text='Requerido.')

    forgot = forms.CharField(max_length=50, required=True,
                             help_text='Requerido. Introduce una pista para recordar tu contraseña')

    info = forms.CharField(max_length=1000, required=False,
                           help_text='Requerido. 1000 caracteres o menos. Presenta brevemente tu empresa.')

    class Meta:
        model = UsuarioLogin
        fields = ('email', 'username', 'password1', 'password2', 'cif', 'telf', 'a_fund','website', 'logo', 'forgot', 'info')