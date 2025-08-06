from rest_framework import serializers

from .models import Actor, Nationality


class NationalityRetrieveCreateUpdateDestroySerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Nationality
        fields = "__all__"


class NationalityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = ["name", "acronym"]


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["first_name", "last_name"]


class ActorRetrieveSerializer(serializers.ModelSerializer):
    nationality = NationalityRetrieveCreateUpdateDestroySerializer(
        read_only=True
    )

    class Meta:
        model = Actor
        fields = "__all__"


class ActorCreateUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"
