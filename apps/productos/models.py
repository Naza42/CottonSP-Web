from django.db import models

class Producto(models.Model):
    imagen = models.ImageField(upload_to='productos/')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    resumen = models.TextField()

    def __str__(self):
        return self.titulo
