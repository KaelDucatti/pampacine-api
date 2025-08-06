from django.contrib import admin

from .models import Actor, Nationality


@admin.register(Actor)
class ActorsAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "nationality", "birthday")
    search_fields = (
        "first_name",
        "last_name",
        "nationality__name",
        "nationality__acronym",
        "birthday",
    )


@admin.register(Nationality)
class NationalitiesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "acronym")
    search_fields = ("name", "acronym")
