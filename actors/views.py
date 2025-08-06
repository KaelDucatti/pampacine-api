from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Actor, Nationality
from .serializers import (
    ActorCreateUpdateDestroySerializer,
    ActorListSerializer,
    ActorRetrieveSerializer,
    NationalityListSerializer,
    NationalityRetrieveCreateUpdateDestroySerializer,
)


class ActorListCreateAPIView(ListCreateAPIView):
    queryset = Actor.objects.select_related("nationality").all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ActorListSerializer
        return ActorCreateUpdateDestroySerializer


class ActorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.select_related("nationality").all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ActorRetrieveSerializer
        return ActorCreateUpdateDestroySerializer


class NationalityListCreateAPIView(ListCreateAPIView):
    queryset = Nationality.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return NationalityListSerializer
        return NationalityRetrieveCreateUpdateDestroySerializer


class NationalityRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Nationality.objects.all()
    serializer_class = NationalityRetrieveCreateUpdateDestroySerializer
