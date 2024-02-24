from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['titulo', 'descripcion', 'resumen', 'resumen_2', 'url', 'imagen_principal', 'imagen_2', 'imagen_3']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
             'titulo': forms.Textarea(attrs={'class': 'form-control'}),
             'resumen': forms.Textarea(attrs={'class': 'form-control'}), 
              'resumen_2': forms.Textarea(attrs={'class': 'form-control'}),
               'url': forms.Textarea(attrs={'class': 'form-control'}),
        }