import factory

from music.models import Singer, Genre, Album, Song, PlayList


class SingerFactory(factory.django.DjangoModelFactory):
    name = 'los muertos de cristo'

    class Meta:
        model = Singer


class GenreFactory(factory.django.DjangoModelFactory):
    name = 'punk'

    class Meta:
        model = Genre


class AlbumFactory(factory.django.DjangoModelFactory):
    name = 'los olvidados'
    singer = factory.SubFactory(SingerFactory)

    class Meta:
        model = Album


class SongFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    album = factory.SubFactory(AlbumFactory)
    genre = factory.SubFactory(GenreFactory)
    duration = 147
    score = 5

    class Meta:
        model = Song


class PlayListFactory(factory.django.DjangoModelFactory):
    name = 'ruido'
    owner = factory.SubFactory('accounts.tests.factories.UserFactory')

    class Meta:
        model = PlayList

    @factory.post_generation
    def songs(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for song in extracted:
                self.songs.add(song)
