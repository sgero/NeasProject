from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioLogin


class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True,
                             help_text='Requerido. Ingrese una dirección de correo electrónico válida.')
    username = forms.CharField(max_length=255, required=True,
                               help_text='Requerido. 255 caracteres o menos. Solo letras, números y @/./+/-/_ caracteres.')
    password = forms.PasswordInput()
    password_confirmation = forms.PasswordInput()

    class Meta:
        model = UsuarioLogin
        fields = ('email', 'username', 'password1', 'password2')