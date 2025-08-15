from django.urls import path

from .views import GenreListCreateAPIView, GenreRetriveUpdateDestroyAPIView

urlpatterns = [
    path(
        "genres/",
        GenreListCreateAPIView.as_view(),
        name="genre_list_create",
    ),
    path(
        "genres/<int:pk>/",
        GenreRetriveUpdateDestroyAPIView.as_view(),
        name="genre_retrieve_update_destroy",
    ),
]
