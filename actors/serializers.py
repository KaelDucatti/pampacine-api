from rest_framework import serializers

from .models import Actor, Nationality


class ActorSerializer(serializers.ModelSerializer):
    nationality = serializers.StringRelatedField()

    class Meta:
        model = Actor
        fields = "__all__"


class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = "__all__"
