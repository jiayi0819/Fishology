from rest_framework import serializers

from fish.models import Fish


class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = (
            "id",
            "name",
            "description",
            "image",
            "model",
            "price",
            "get_image",
            "get_lock_image",
            "get_model"
        )
