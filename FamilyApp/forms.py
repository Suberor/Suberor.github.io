from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from FamilyApp.models import Avatar, Spells


class SpellsFormulario(forms.Form):

    nombre = forms.CharField()
    nivel = forms.IntegerField()
    escuela = forms.CharField()  
    descripcion = forms.CharField()
    imagen = forms.ImageField()

class MonstersFormulario(forms.Form):

    nombre = forms.CharField()
    nivel_desafio = forms.IntegerField()
    terreno = forms.CharField()

class WeaponsFormulario(forms.Form):

    nombre = forms.CharField()
    tipo = forms.CharField()
    versatil = forms.BooleanField()
    legendaria = forms.BooleanField()
    descripcion = forms.CharField()
    puntaje = forms.FloatField()
    opinion = forms.CharField()
    imagen = forms.ImageField()


class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Ingrese nuevamente la contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "password1", "password2"]


class EditarFormulario( UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Ingrese nuevamente la contraseña", widget=forms.PasswordInput)
 
    class Meta:

        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]

    
class AvatarFormulario(forms.ModelForm):

    class Meta:

        model = Avatar
        fields = ["imagen"]


class ReseñasFormulario(forms.Form):

    model = Spells
    nombre = forms.CharField()
    puntaje = forms.FloatField()
    opinion = forms.CharField()