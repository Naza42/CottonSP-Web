from django import forms
from .models import Noticia, Comment
from django.forms import ModelForm, TextInput
from django.forms.widgets import TextInput, FileInput, Select


class NoticiaForm(forms.ModelForm):
    
    class Meta:
        model = Noticia
        fields = ['titulo', 'resumen', 'contenido', 'imagen', 'categoria_noticia']
        widgets = {
            'titulo': TextInput(attrs={'class': 'form-control'}),
            'resumen': TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': FileInput(attrs={'class': 'form-control'}),
            'categoria_noticia': Select(attrs={'class': 'form-control'}),
        }


# CREAR COMENTARIOS
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text'] #campos de mi formulario
        exclude = ['author']
        widgets = {
        'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu comentario aquí...'}),
    }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CommentForm, self).__init__(*args, **kwargs)
        if user:
            self.instance.author = user.username