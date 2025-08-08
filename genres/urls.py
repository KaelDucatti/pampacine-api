from django.urls import path

from .views import GenreListCreateAPIView, GenreRetriveUpdateDestroyAPIView

urlpatterns = [
    path(
        "genres/",
        GenreListCreateAPIView.as_view(),
        name="genre-list-create",
    ),
    path(
        "genres/<int:pk>/",
        GenreRetriveUpdateDestroyAPIView.as_view(),
        name="genre-retrieve-update-destroy",
    ),
]
