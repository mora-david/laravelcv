from rest_framework import serializers
from .models import Artista

class ArtistaSerializer(serializers.ModelSerializer):
    """
    General purpose Autor serializer
    """
    class Meta:
        model = Artista
        fields = ('id', 'nombre')