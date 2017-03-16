from django.db import models


class SlugModel(models.Model):
    name = models.CharField(max_length=100)
    name_slug = models.SlugField(max_length=100)

    class Meta:
        abstract = True


class Singer(SlugModel):
    pass


class Genre(SlugModel):
    pass


class Album(SlugModel):
    singer = models.ForeignKey(Singer, related_name='albums')


class Song(SlugModel):
    album = models.ForeignKey(Album, related_name='songs')
    genre = models.ForeignKey(Genre, related_name='genres')
    duration = models.PositiveIntegerField()
    score = models.PositiveIntegerField(default=0)


class PlayList(SlugModel):
    owner = models.ForeignKey('accounts.User', related_name='playlists')
    songs = models.ManyToManyField(Song, related_name='playlists')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
