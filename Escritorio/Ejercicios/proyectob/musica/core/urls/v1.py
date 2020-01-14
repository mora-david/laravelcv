from rest_framework import routers
from django.conf.urls import url, include
from artistas.views import ArtistaViewSet
from canciones.views import CancionViewSet
from Albumes.views import AlbumesViewSet

router = routers.DefaultRouter()
router.register(r'artistas', ArtistaViewSet)
router.register(r'canciones', CancionViewSet)
router.register(r'albumes', AlbumesViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]