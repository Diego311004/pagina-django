from django.db import models

# Create your models here.
# makemigrations
# migrate 



class Entrada(models.Model):
    nombre = models.CharField(max_length=50)
    contenido = models.TextField(max_length=800)
    imagen = models.URLField()
    autor = models.CharField(max_length=50)


    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    nombre = models.CharField(max_length=60)
    Comentario = models.TextField(max_length=400)
    
    def __str__(self):
        return self.nombre




   
