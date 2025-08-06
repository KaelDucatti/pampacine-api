from rest_framework import serializers

from .models import Genre


class GenreRetrieveCreateUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name"]
