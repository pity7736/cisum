from django.conf.urls import include, url

from rest_framework import routers

from music.views import SongViewSet, SingerViewSet, GenreViewSet, AlbumViewSet, PlayListViewSet


router = routers.DefaultRouter()
router.register(r'singers', SingerViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'songs', SongViewSet)
router.register(r'playlists', PlayListViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
