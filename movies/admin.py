from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "release_date",
        "resume",
    )
    search_fields = ("title", "release_date", "movie_cast", "genres")
