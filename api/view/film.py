from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    ListAPIView, RetrieveAPIView

from api.permissions import UserStaffPermission, UserAPIPermission
from film.models import Film, Genre
from film.serializers import FilmSerializer, GenreSerializer


class FilmListAPIView(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [UserAPIPermission]


class FilmCreateAPIView(ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [UserStaffPermission]


class FilmDetailAPIView(RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [UserAPIPermission]


class FilmRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [UserStaffPermission]


class GenreListAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [UserStaffPermission]


class GenreRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [UserStaffPermission]
