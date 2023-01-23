from rest_framework import serializers
# from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

from account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'email',
            'bio',
            'birthday',
            'image',
            'get_image'
        )
