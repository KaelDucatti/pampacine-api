from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Genre
from .serializers import GenreSerializer


class GenreListCreateView(ListCreateAPIView):
    queryset = Genre.objects.filter(active=True)
    serializer_class = GenreSerializer


class GenreRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
