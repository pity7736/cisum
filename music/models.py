from django.db import models
from django.utils.text import slugify


class SlugModel(models.Model):
    name = models.CharField(max_length=100)
    name_slug = models.SlugField(max_length=100)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(SlugModel, self).save(*args, **kwargs)


class Singer(SlugModel):

    def __str__(self):
        return self.name


class Genre(SlugModel):

    def __str__(self):
        return self.name


class Album(SlugModel):
    singer = models.ForeignKey(Singer, related_name='albums')

    def __str__(self):
        return '{} - {}'.format(self.name, self.singer.name)


class Song(SlugModel):
    album = models.ForeignKey(Album, related_name='songs')
    genre = models.ForeignKey(Genre, related_name='genres')
    duration = models.PositiveIntegerField()
    score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{} - {}'.format(self.name, self.album.__str__())


class PlayList(SlugModel):
    owner = models.ForeignKey('accounts.User', related_name='playlists')
    songs = models.ManyToManyField(Song, related_name='playlists')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.owner.get_full_name())
