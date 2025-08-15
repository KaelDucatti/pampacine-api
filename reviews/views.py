from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Review
from .serializers import (
    ReviewCreateUpdateDestroySerializer,
    ReviewListSerializer,
    ReviewRetrieveSerializer,
)


class ReviewListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Review.objects.select_related("movie").all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReviewListSerializer
        return ReviewCreateUpdateDestroySerializer


class ReviewRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Review.objects.select_related("movie").all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReviewRetrieveSerializer
        return ReviewCreateUpdateDestroySerializer
