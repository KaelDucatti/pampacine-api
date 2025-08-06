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
    search_fields = (
        "title",
        "movie_cast__first_name",
        "movie_cast__last_name",
        "genres__name",
    )
