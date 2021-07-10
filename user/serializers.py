from rest_framework import serializers

from user.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """User Profile Serializer implementation"""
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """User Serializer implementation"""

    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'

