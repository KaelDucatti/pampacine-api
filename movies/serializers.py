from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField()

    class Meta:
        model = Movie
        fields = "__all__"
