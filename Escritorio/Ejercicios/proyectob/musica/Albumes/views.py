from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import AlbumesSerializer
from .models import Albumes

class AlbumesViewSet(viewsets.ModelViewSet):
    queryset = Albumes.objects.all()
    serializer_class = AlbumesSerializer
