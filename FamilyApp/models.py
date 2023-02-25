from django.db import models
from django.contrib.auth.models import User
 

class Spells(models.Model):

    nombre = models.CharField(max_length=30)
    nivel = models.IntegerField()
    escuela = models.CharField(max_length=30)    
    descripcion = models.TextField(max_length=200, default="")
    imagen = models.ImageField(default="FamilyApp/assets/img/blank.png")
    

    def __str__(self):

        return f"{self.nombre}"

class Monsters(models.Model):

    nombre = models.CharField(max_length=30)
    nivel_desafio = models.IntegerField()
    terreno = models.CharField(max_length=30)

    def __str__(self):

        return f"{self.nombre}"

class Weapons(models.Model):

    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    versatil = models.BooleanField()
    legendaria = models.BooleanField(default=False)
    descripcion = models.TextField(max_length=200, default="")
    puntaje = models.FloatField(default=0)
    opinion = models.TextField(max_length=200, default="")
    imagen = models.ImageField(upload_to="FamilyApp/assets/img/", default="FamilyApp/assets/img/blank.png")

    def __str__(self):

        return f"{self.nombre}"

class Avatar(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

class SpellsReseñas(models.Model):

    usuario=models.CharField(max_length=40, default="")
    nombre=models.CharField(max_length=40, default="")
    puntaje = models.FloatField(default=0)
    opinion = models.TextField(max_length=200, default="")
    


