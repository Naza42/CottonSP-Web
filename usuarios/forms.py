from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(label='Correo', required=True,widget=forms.TextInput(attrs={'class': 'form-control item' }) )
    first_name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(attrs={'class': 'form-control item' }))
    last_name = forms.CharField(label='Apellido', required=True, widget=forms.TextInput(attrs={'class': 'form-control item' }))
    username = forms.CharField(label='Nombre de usuario', required=True, widget=forms.TextInput(attrs={'class': 'form-control item' }))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control item'  }), required=True)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control item'  }), required=True )



    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]

        
