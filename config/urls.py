from django.contrib import admin
from django.urls import path

from genres.views import GenreListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/genres/", GenreListView, name="genre-list"),
    path("api/v1/genres/<int:pk>/", ..., name="genre-detail"),
]
