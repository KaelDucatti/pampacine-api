from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Genre
from .serializers import GenreRetrieveCreateUpdateDestroySerializer


class GenreListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Genre.objects.filter(active=True)
    serializer_class = GenreRetrieveCreateUpdateDestroySerializer


class GenreRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Genre.objects.all()
    serializer_class = GenreRetrieveCreateUpdateDestroySerializer
