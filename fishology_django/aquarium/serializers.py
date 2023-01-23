from rest_framework import serializers

from aquarium.models import Aquarium
from account.serializers import UserSerializer


class AquariumSerializer(serializers.ModelSerializer):
    # participants = serializers.CharField(source='participants.username')
    # participants = serializers.CharField(source='.name')
    participants = serializers.StringRelatedField(many=True)
    host = UserSerializer()

    class Meta:
        model = Aquarium
        fields = (
            "id",
            "host",
            "participants",
            "name",
            "description",
            "image",
            "created",
            "updated",
            "sky",
            "scene",
            "isPrivate",
            "get_absolute_url",
            "get_total_fish",
            "get_image"
        )
