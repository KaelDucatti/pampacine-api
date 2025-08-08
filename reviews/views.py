from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Review
from .serializers import (
    ReviewCreateUpdateDestroySerializer,
    ReviewListSerializer,
    ReviewRetrieveSerializer,
)


class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.select_related("movie").all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReviewListSerializer
        return ReviewCreateUpdateDestroySerializer


class ReviewRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.select_related("movie").all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReviewRetrieveSerializer
        return ReviewCreateUpdateDestroySerializer
