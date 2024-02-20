from django.db import models

class Producto(models.Model):
    imagen_principal = models.ImageField(upload_to='productos/',blank=False,null=False)
    imagen_2 = models.ImageField(upload_to='productos/',blank=True,null=True,default='img/hero-banner.jpg')
    imagen_3 = models.ImageField(upload_to='productos/',blank=True,null=True,default='img/hero-banner.jpg')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length = 256)
    resumen = models.TextField(max_length = 256,blank = True)
    resumen_2 = models.TextField(max_length = 256,blank = True)
    url = models.URLField(blank = True,null = True)
    def __str__(self):
        return self.titulo
    def delete(self):
        if self.imagen_2.name != 'img/hero-banner.jpg':
            self.imagen_2.delete(self.imagen_2)
        if  self.imagen_3.name != 'img/hero-banner.jpg':
            self.imagen_3.delete(self.imagen_3)
        super().delete()