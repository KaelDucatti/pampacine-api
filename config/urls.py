from django.contrib import admin
from django.urls import path

from actors.views import (
    ActorListCreateAPIView,
    ActorRetrieveUpdateDestroyAPIView,
    NationalityListCreateAPIView,
    NationalityRetrieveUpdateDestroyAPIView,
)
from genres.views import (
    GenreListCreateAPIView,
    GenreRetriveUpdateDestroyAPIView,
)
from movies.views import (
    MovieListCreateAPIView,
    MovieRetrieveUpdateDestroyAPIView,
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
        name="genre-retrieve-update-destroy",
    ),
    path(
        "api/v1/actors/",
        ActorListCreateAPIView.as_view(),
        name="actor-list-create",
    ),
    path(
        "api/v1/actors/<int:pk>/",
        ActorRetrieveUpdateDestroyAPIView.as_view(),
        name="actor-retrieve-update-destroy",
    ),
    path(
        "api/v1/nationality/",
        NationalityListCreateAPIView.as_view(),
        name="nationality-list-create",
    ),
    path(
        "api/v1/nationality/<int:pk>/",
        NationalityRetrieveUpdateDestroyAPIView.as_view(),
        name="nationality-retrieve-update-destroy",
    ),
    path(
        "api/v1/movies/",
        MovieListCreateAPIView.as_view(),
        name="movies-list-create",
    ),
    path(
        "api/v1/movies/<int:pk>/",
        MovieRetrieveUpdateDestroyAPIView.as_view(),
        name="movies-retreive-update-destroy",
    ),
]
