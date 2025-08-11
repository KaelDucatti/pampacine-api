from rest_framework import serializers

from actors.serializers import ActorRetrieveSerializer
from genres.serializers import (
    GenreRetrieveCreateUpdateDestroySerializer,
)

from .models import Movie


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True, read_only=True)
    movie_cast = serializers.StringRelatedField(many=True, read_only=True)
    rate = serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "release_date",
            "genres",
            "movie_cast",
            "rate",
            "reviews",
        ]

    def get_rate(self, obj):
        reviews = obj.movie_reviews.all()
        result = (
            sum(r.stars for r in reviews) / reviews.count() if reviews else 0
        )
        return round(result, 2)

    def get_reviews(self, obj):
        return len(obj.movie_reviews.all())


class MovieRetrieveSerializer(serializers.ModelSerializer):
    genres = GenreRetrieveCreateUpdateDestroySerializer(
        many=True, read_only=True
    )
    movie_cast = ActorRetrieveSerializer(many=True, read_only=True)
    rate = serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def get_rate(self, obj):
        reviews = obj.movie_reviews.all()
        result = sum(r.stars for r in reviews) / len(reviews)
        return round(result, 2) if reviews else 0

    def get_reviews(self, obj):
        return len(obj.movie_reviews.all())


class MovieCreateUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError(
                "A data de lançamento não pode ser inferior a 1900."
            )
        return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError(
                "O resumo não pode ultrapassar 200 caracteres."
            )
        return value
