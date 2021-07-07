from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, ListCreateAPIView

from user.models import UserProfile
from user.serializers import UserSerializer


class UserListAPIView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
