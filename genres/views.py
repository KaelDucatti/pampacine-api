from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Genre
from .serializers import GenreRetrieveCreateUpdateDestroySerializer


class GenreListCreateAPIView(ListCreateAPIView):
    queryset = Genre.objects.filter(active=True)
    serializer_class = GenreRetrieveCreateUpdateDestroySerializer


class GenreRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreRetrieveCreateUpdateDestroySerializer
