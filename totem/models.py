from django.db import models
from operator import mod
from django.db import models
# Create your models here.

class Totem(models.Model):
    paciente = models.CharField(max_length=100)
    senha = models.CharField(max_length=200)
    sala = models.IntegerField()
    data =models.DateField()