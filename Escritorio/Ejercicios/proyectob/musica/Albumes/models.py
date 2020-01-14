from django.db import models

from artistas.models import Artista
from django.utils import timezone


class Albumes(models.Model):
    nombre = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, default=0)