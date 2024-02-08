from django.db import models

class Producto(models.Model):

    codigo = models.IntegerField()
    nombre = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} - {self.codigo}'
