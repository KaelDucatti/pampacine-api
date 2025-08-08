from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "movie__title", "stars", "comment")
    search_fields = ("movie__title", "stars")
