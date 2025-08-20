from django.db.models import Avg, Count
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from config.permissions import GlobalDefaultPermission
from reviews.models import Review

from .models import Movie
from .serializers import (
    MovieCreateUpdateDestroySerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
)


class MovieListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission)
    queryset = Movie.objects.prefetch_related("movie_cast", "genres").all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieListSerializer
        return MovieCreateUpdateDestroySerializer


class MovieRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission)
    queryset = Movie.objects.prefetch_related(
        "movie_cast__nationality", "genres"
    ).all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieRetrieveSerializer
        return MovieCreateUpdateDestroySerializer


class MovieStatsAPIView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movie_by_gender = (
            self.queryset.values("genres__id", "genres__name")
            .annotate(movie_count=Count("id", distinct=True))
            .order_by("-movie_count")
        )

        total_reviews = Review.objects.count()
        average_stars = (
            Review.objects.values("movie__genres__id", "movie__genres__name")
            .annotate(avg_stars=Avg("stars"))
            .order_by("-avg_stars")
        )

        return Response(
            data={
                "total_movies": total_movies,
                "movie_stats": {
                    "total_reviews": total_reviews,
                    "avg_stars_by_genre": list(average_stars),
                    "movie_by_genre": list(movie_by_gender),
                },
            },
            status=status.HTTP_200_OK,
        )
