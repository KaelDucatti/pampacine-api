from django.contrib import admin
from django.urls import path

from actors.views import (
    ActorListCreateAPIView,
    ActorRetriveUpdateDestroyAPIView,
)
from genres.views import (
    GenreListCreateAPIView,
    GenreRetriveUpdateDestroyAPIView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/v1/genres/",
        GenreListCreateAPIView.as_view(),
        name="genre-list-create",
    ),
    path(
        "api/v1/genres/<int:pk>/",
        GenreRetriveUpdateDestroyAPIView.as_view(),
        name="genre-retrive-update-destroy",
    ),
    path(
        "api/v1/actors/",
        ActorListCreateAPIView.as_view(),
        name="actor-list-create",
    ),
    path(
        "api/v1/actors/<int:pk>/",
        ActorRetriveUpdateDestroyAPIView.as_view(),
        name="actor-retrive-update-destroy",
    ),
]
