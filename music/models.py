from django.db import models              #django.DATABASE
from django.core.urlresolvers import reverse


class Album(models.Model):     # This will become a table in the database   AND all classes that wanna become table must "inherit" from models.Model
    artist = models.CharField(max_length = 250)
    album_title = models.CharField(max_length = 500)
    genre = models.CharField(max_length = 100)
    album_logo = models.FileField()


    def __str__(self):   # Remember the indentation matters, this function was supposed to be inside the Album class as it works for Album >:(
        return self.artist + " - " + self.album_title

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})   #or self.id


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)                 #this on_delete just says that when an album is deleted, delete all the songs linked to it .!.
    file_type = models.CharField(max_length = 10)
    song_title = models.CharField(max_length = 250)
    is_favorite = models.BooleanField(default = False)

    def __str__(self):
        return self.song_title
