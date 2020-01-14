from rest_framework import serializers
from .models import Albumes
from artistas.serializers import ArtistaSerializer


class AlbumesSerializer(serializers.ModelSerializer):
    """
    General purtpose serializer
    """
    artista = ArtistaSerializer(read_only=True)

    class Meta:
        model = Albumes
        fields = ("artista",'nombre',)
