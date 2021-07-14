from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView

from api.permissions import UserStaffPermission, UserOwnerPermission, ProfileOwnerPermission
from user.models import UserProfile
from user.serializers import UserSerializer, UserProfileSerializer


class UserListAPIView(ListAPIView):
    """User List API for admin implementation"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserStaffPermission]


class UserRetrieveAPIView(RetrieveUpdateAPIView):
    """User Retrieve API for owner implementation"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserOwnerPermission]


class UserProfileRetrieveAPIView(RetrieveUpdateAPIView):
    """UserProfile Retrieve API for owner implementation"""

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [ProfileOwnerPermission]
