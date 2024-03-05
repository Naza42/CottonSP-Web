from django.db import models
from ckeditor.fields import RichTextField
from apps.noticias.models import Categoria
class Producto(models.Model):
    imagen_principal = models.ImageField(upload_to='productos/',blank=False,null=False)
    imagen_2 = models.ImageField(upload_to='productos/',blank=True,null=True,default='img/hero-banner.jpg')
    imagen_3 = models.ImageField(upload_to='productos/',blank=True,null=True,default='img/hero-banner.jpg')
    titulo = models.CharField(max_length=100)
    descripcion = RichTextField(max_length = 700)
    resumen = RichTextField(max_length = 256,blank = True)
    resumen_2 = RichTextField(max_length = 700,blank = True)
    url = models.URLField(blank = True,null = True)
    categoria = models.ForeignKey(Categoria,null = True,on_delete = models.DO_NOTHING, default = None)
    def __str__(self):
        return self.titulo
    def delete(self):
        if self.imagen_2.name != 'img/hero-banner.jpg':
            self.imagen_2.delete(self.imagen_2)
        if  self.imagen_3.name != 'img/hero-banner.jpg':
            self.imagen_3.delete(self.imagen_3)
        super().delete()