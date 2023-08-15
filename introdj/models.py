from django.db import models

# Create your models here.

class Auto(models.Model):

    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    fecha = models.DateField(auto_now=True)
