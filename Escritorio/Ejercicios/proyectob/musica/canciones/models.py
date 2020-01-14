from django.db import models

# Create your models here.
from artistas.models import Artista


class Cancion(models.Model):
    nombre = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
