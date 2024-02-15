from django.contrib import admin
from .models import Noticia, Comment, Categoria

admin.site.register(Noticia)
admin.site.register(Comment)
admin.site.register(Categoria)
