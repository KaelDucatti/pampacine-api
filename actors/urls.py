from django.urls import path

from .views import (
    ActorListCreateAPIView,
    ActorRetrieveUpdateDestroyAPIView,
    NationalityListCreateAPIView,
    NationalityRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path(
        "actors/",
        ActorListCreateAPIView.as_view(),
        name="actor-list-create",
    ),
    path(
        "actors/<int:pk>/",
        ActorRetrieveUpdateDestroyAPIView.as_view(),
        name="actor-retrieve-update-destroy",
    ),
    path(
        "nationality/",
        NationalityListCreateAPIView.as_view(),
        name="nationality-list-create",
    ),
    path(
        "nationality/<int:pk>/",
        NationalityRetrieveUpdateDestroyAPIView.as_view(),
        name="nationality-retrieve-update-destroy",
    ),
]
