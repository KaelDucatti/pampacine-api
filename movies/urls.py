from django.urls import path

from .views import MovieListCreateAPIView, MovieRetrieveUpdateDestroyAPIView

urlpatterns = [
    path(
        "movies/",
        MovieListCreateAPIView.as_view(),
        name="movies-list-create",
    ),
    path(
        "movies/<int:pk>/",
        MovieRetrieveUpdateDestroyAPIView.as_view(),
        name="movies-retreive-update-destroy",
    ),
]
