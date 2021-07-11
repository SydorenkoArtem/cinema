from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.response import Response

from api.permissions import UserPermission
from user.models import UserProfile
from user.serializers import UserSerializer


class UserListAPIView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]
