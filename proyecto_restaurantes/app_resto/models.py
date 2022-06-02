from django.db import models

class Restaurante(models.Model):

    nombre = models.CharField(max_length=40)
    categoria = models.CharField(max_length=40)
    ubicacion = models.CharField(max_length=40)
    capacidad = models.IntegerField()

class Platos(models.Model):

    plato = models.CharField(max_length=40)
    categoria = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    precio = models.IntegerField()

class Reseñas(models.Model):
    
    plato = models.CharField(max_length=40)
    sabor = models.IntegerField()
    presentacion = models.IntegerField()
    calidad_precio= models.IntegerField()
