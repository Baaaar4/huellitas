from django import forms
from django.forms import ModelForm
from .models import Atencion, Mascota, Dueno

class AtenForm(ModelForm):
    class Meta:
        model = Atencion
        fields = ['descripcion', 'peluqueria', 'medicamentos']

class NewMascota(ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'tipo', 'raza', 'patologias', 'dueno' ]

class NewDueno(ModelForm):
    class Meta:
        model = Dueno
        fields = ['nombre', 'apellido', 'rut', 'telefono', 'direccion' ]

class LoginForm(forms.Form):
    email = forms.CharField(
        max_length=250, min_length=3, label='Ingrese su nombre de usuario')
    password = forms.CharField(min_length=8, max_length=16,
                               label='Ingrese su contraseña', widget=forms.PasswordInput())