from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView

from film.models import Film, Genre
from film.serializers import FilmSerializer, GenreSerializer


class FilmListAPIView(ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class FilmRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class GenreListAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
