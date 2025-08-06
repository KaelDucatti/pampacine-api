from rest_framework import serializers

from actors.serializers import ActorRetrieveSerializer
from genres.serializers import (
    GenreRetrieveCreateUpdateDestroySerializer,
)

from .models import Movie


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True, read_only=True)
    movie_cast = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "release_date", "genres", "movie_cast"]


class MovieRetrieveSerializer(serializers.ModelSerializer):
    genres = GenreRetrieveCreateUpdateDestroySerializer(
        many=True, read_only=True
    )
    movie_cast = ActorRetrieveSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"


class MovieCreateUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
