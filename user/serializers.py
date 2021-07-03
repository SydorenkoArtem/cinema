from rest_framework import serializers

from user.models import UserProfile


class UserProfielSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profile =
