from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    ListAPIView, RetrieveAPIView

from api.permissions import UserStaffPermission, UserAPIPermission
from film.models import Film, Genre
from film.serializers import FilmSerializer, GenreSerializer


class FilmListAPIView(ListAPIView):
    """Film List API for user implementation"""

    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [UserAPIPermission]


class FilmCreateAPIView(ListCreateAPIView):
    """Film ListCreate API for admin implementation"""

    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [UserStaffPermission]


class FilmDetailAPIView(RetrieveAPIView):
    """Film Retrieve API for user implementation"""

    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [UserAPIPermission]


class FilmRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    """Film RetrieveUpdate API for admin implementation"""

    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [UserStaffPermission]


class GenreListAPIView(ListCreateAPIView):
    """Genre List API implementation"""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [UserStaffPermission]


class GenreRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """Genre Retrieve Update API implementation"""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [UserStaffPermission]
