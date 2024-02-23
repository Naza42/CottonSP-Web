from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['titulo','descripcion','resumen','resumen_2','url','imagen_principal','imagen_2','imagen_3']
