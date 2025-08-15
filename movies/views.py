from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from .models import Movie
from .serializers import (
    MovieCreateUpdateDestroySerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
)


class MovieListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.prefetch_related("movie_cast", "genres").all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieListSerializer
        return MovieCreateUpdateDestroySerializer


class MovieRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.prefetch_related(
        "movie_cast__nationality", "genres"
    ).all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieRetrieveSerializer
        return MovieCreateUpdateDestroySerializer
