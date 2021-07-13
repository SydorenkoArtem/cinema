from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView

from api.permissions import UserStaffPermission, UserOwnerPermission, ProfileOwnerPermission
from user.models import UserProfile
from user.serializers import UserSerializer, UserProfileSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserStaffPermission]


class UserRetrieveAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserOwnerPermission]


class UserProfileRetrieveAPIView(RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [ProfileOwnerPermission]
