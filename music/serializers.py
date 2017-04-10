from rest_framework.serializers import HyperlinkedModelSerializer

from music.models import Song, Singer, Genre, Album, PlayList


class SingerSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Singer
        fields = '__all__'


class GenreSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class AlbumSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Album
        fields = '__all__'


class SongSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'


class PlayListSerializer(HyperlinkedModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = PlayList
        fields = '__all__'
