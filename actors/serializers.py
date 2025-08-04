from rest_framework import serializers

from .models import Actor, Nationality


class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = "__all__"


class ActorListSerializer(serializers.ModelSerializer):
    nationality = NationalitySerializer(read_only=True)

    class Meta:
        model = Actor
        fields = "__all__"


class ActorCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"
