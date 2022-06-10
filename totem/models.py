from django.db import models

# Create your models here.

class Totem(models.Model):
    paciente = models.CharField(max_length=50)
    senha = models.CharField(max_length=20)
    sala = models.IntegerField()
    horario = models.DateTimeField("Data/Hora Chegada", auto_now_add=True)
