from django.contrib import admin
from django.urls import path

from genres.views import GenreListCreateView, GenreRetriveUpdateDestroyView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/v1/genres/",
        GenreListCreateView.as_view(),
        name="genre-list-create",
    ),
    path(
        "api/v1/genres/<int:pk>/",
        GenreRetriveUpdateDestroyView.as_view(),
        name="genre-detail",
    ),
]
