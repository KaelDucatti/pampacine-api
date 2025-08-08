from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from movies.models import Movie

START_CHOICES = [
    (0, "O estrelas"),
    (1, "1 estrela"),
    (2, "2 estrelas"),
    (3, "3 estrelas"),
    (4, "4 estrelas"),
    (5, "5 estrelas"),
]


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(
        Movie, on_delete=models.PROTECT, related_name="movie_reviews"
    )
    stars = models.IntegerField(
        choices=START_CHOICES,
        validators=[
            MinValueValidator(0, "Mínino 0"),
            MaxValueValidator(5, "Máximo 5"),
        ],
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.movie} ({self.stars}) estrelas"

    class Meta:
        ordering = ["movie__title"]
        verbose_name_plural = "Reviews"
