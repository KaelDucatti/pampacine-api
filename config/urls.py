from django.contrib import admin
from django.urls import path

from genres.views import GenreListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/genre/", GenreListView.as_view(), name="genre-list"),
]
