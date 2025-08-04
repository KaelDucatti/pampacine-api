from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Actor, Nationality
from .serializers import (
    ActorCreateUpdateSerializer,
    ActorListSerializer,
    NationalitySerializer,
)


class ActorListCreateAPIView(ListCreateAPIView):
    queryset = Actor.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ActorListSerializer
        return ActorCreateUpdateSerializer


class ActorRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ActorListSerializer
        return ActorCreateUpdateSerializer


class NationalityListCreateAPIView(ListCreateAPIView):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer


class NationalityRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer
