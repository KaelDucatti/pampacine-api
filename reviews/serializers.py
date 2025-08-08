from rest_framework import serializers

from movies.serializers import MovieListSerializer

from .models import Review


class ReviewListSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"


class ReviewRetrieveSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"


class ReviewCreateUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
