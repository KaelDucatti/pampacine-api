from django.db import models

from actors.models import Actor
from genres.models import Genre


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    release_date = models.DateField(null=True, blank=True)
    movie_cast = models.ManyToManyField(Actor, related_name="movie-cast")
    resume = models.TextField(null=True, blank=True)
    genres = models.ForeignKey(
        Genre, on_delete=models.PROTECT, related_name="movie-genres"
    )

    def __str__(self):
        return self.title
