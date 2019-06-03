from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
	password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, help_text="Ingrese la misma contraseña que antes para validación")
	class Meta:
		model = User
		fields = ['first_name','last_name','username','password1','password2']
		labels = {
			'first_name': 'Nombre',
			'last_name': 'Apellido',
			'username': 'Nombre de usuario',
		}
		help_texts = {
			'username': 'Campo requerido. 150 caracteres o menos. Letras, digitos y @/./+/-/_ solamente.',
		}


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['is_guardia','is_admin']
		labels = {
			'is_guardia': 'Guardia',
			'is_admin': 'Administrador',
		}