from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from music.models import Song, Singer, Genre, Album, PlayList
from music.serializers import SongSerializer, SingerSerializer, GenreSerializer, AlbumSerializer, PlayListSerializer


class SingerViewSet(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class PlayListViewSet(ModelViewSet):
    queryset = PlayList.objects.all()
    serializer_class = PlayListSerializer
    authentication_classes = (BasicAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.playlists.all()
