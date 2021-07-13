from django.contrib.auth.models import User
from rest_framework import serializers

from user.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """User Profile Serializer implementation"""
    id = serializers.IntegerField(read_only=True)
    avatar = serializers.ImageField(
        max_length=None, use_url=True,
    )

    class Meta:
        model = UserProfile
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    """User Serializer implementation"""
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "last_login", "username", "first_name", "last_name", "email"]
