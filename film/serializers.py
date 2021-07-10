from rest_framework import serializers

from film.models import Film, Genre


class FilmSerializer(serializers.ModelSerializer):
    """Film Serializer implementation"""

    class Meta:
        model = Film
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    """Genre Serializer implementation"""

    class Meta:
        model = Genre
        fields = '__all__'

