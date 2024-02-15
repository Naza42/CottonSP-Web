from django import forms
from .models import Contacto
from django.forms import ModelForm, TextInput


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        #fields = ['nombre', 'correo', 'mensaje']
        fields = '__all__'
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'correo': TextInput(attrs={'class': 'form-control'}),
            'tipo_consulta': forms.Select(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
            'avisos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    
