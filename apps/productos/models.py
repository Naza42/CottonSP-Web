from django.db import models

class Producto(models.Model):
    imagen_principal = models.ImageField(upload_to='productos/',default='img/hero-banner.jpg',blank=False,null=False)
    imagen_2 = models.ImageField(upload_to='productos/',blank=True,null=True)
    imagen_3 = models.ImageField(upload_to='productos/',blank=True,null=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length = 256)
    resumen = models.TextField(max_length = 256,blank = True)
    resumen_2 = models.TextField(max_length = 256,blank = True)

    def __str__(self):
        return self.titulo
