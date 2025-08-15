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
        name="actor_list_create",
    ),
    path(
        "actors/<int:pk>/",
        ActorRetrieveUpdateDestroyAPIView.as_view(),
        name="actor_retrieve_update_destroy",
    ),
    path(
        "nationality/",
        NationalityListCreateAPIView.as_view(),
        name="nationality_list_create",
    ),
    path(
        "nationality/<int:pk>/",
        NationalityRetrieveUpdateDestroyAPIView.as_view(),
        name="nationality_retrieve_update_destroy",
    ),
]
