from django.urls import path

from .views import (
    MovieListCreateAPIView,
    MovieRetrieveUpdateDestroyAPIView,
    MovieStatsAPIView,
)

urlpatterns = [
    path(
        "movies/",
        MovieListCreateAPIView.as_view(),
        name="movies_list_create",
    ),
    path(
        "movies/<int:pk>/",
        MovieRetrieveUpdateDestroyAPIView.as_view(),
        name="movies_retreive_update_destroy",
    ),
    path("movies/stats/", MovieStatsAPIView.as_view(), name="movies_stats"),
]
