from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from config.permissions import GlobalDefaultPermission

from .models import Actor, Nationality
from .serializers import (
    ActorCreateUpdateDestroySerializer,
    ActorListSerializer,
    ActorRetrieveSerializer,
    NationalityListSerializer,
    NationalityRetrieveCreateUpdateDestroySerializer,
)


class ActorListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission)
    queryset = Actor.objects.select_related("nationality").all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ActorListSerializer
        return ActorCreateUpdateDestroySerializer


class ActorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission)
    queryset = Actor.objects.select_related("nationality").all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ActorRetrieveSerializer
        return ActorCreateUpdateDestroySerializer


class NationalityListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission)
    queryset = Nationality.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return NationalityListSerializer
        return NationalityRetrieveCreateUpdateDestroySerializer


class NationalityRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission)
    queryset = Nationality.objects.all()
    serializer_class = NationalityRetrieveCreateUpdateDestroySerializer


class ActorStatsAPIView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission)
    queryset = Actor.objects.all()

    def get(self, request, pk):
        actor = get_object_or_404(Actor, pk=pk)
        total_movies = actor.movie_cast.count()

        genre_stats = (
            actor.movie_cast.values("genres__name", "genres__id")
            .annotate(movie_count=Count("id"))
            .order_by("-movie_count", "genres__name")
        )

        return Response(
            {
                "actor": {
                    "id": actor.id,
                    "name": f"{actor.first_name} {actor.last_name}",
                    "total_movies": total_movies,
                },
                "genres_breakdown": list(genre_stats),
            }
        )
