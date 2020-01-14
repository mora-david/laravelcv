from rest_framework import viewsets
from canciones.serializers import CancionSerializer
from canciones.models import Cancion

class CancionViewSet(viewsets.ModelViewSet):
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer
