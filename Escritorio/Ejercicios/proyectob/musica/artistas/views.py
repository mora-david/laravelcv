from rest_framework import viewsets
from artistas.models import Artista
from artistas.serializers import ArtistaSerializer


# Create your views here.
class ArtistaViewSet(viewsets.ModelViewSet):

    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer
