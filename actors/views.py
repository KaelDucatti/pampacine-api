from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Actor, Nationality
from .serializers import ActorSerializer, NationalitySerializer


class ActorListCreateAPIView(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class NationalityListCreateAPIView(ListCreateAPIView):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer


class NationalityRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer
