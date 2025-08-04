from django.db import models


class Nationality(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.name} ({self.acronym})"

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Nationalities"


class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.ForeignKey(
        Nationality,
        on_delete=models.PROTECT,
        related_name="actors_nationality",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["first_name", "last_name"]
        verbose_name_plural = "Actors"
