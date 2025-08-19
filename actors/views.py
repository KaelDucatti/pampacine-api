from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

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
