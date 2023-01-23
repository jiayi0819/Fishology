from rest_framework import serializers
from scene.models import Scene, Sky, Prop


class SceneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scene
        fields = (
            "name",
            "description",
            "image",
            "folder",
            "price",
            "get_image"
        )


class SkySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sky
        fields = (
            "name",
            "description",
            "image",
            "folder",
            "price",
            "get_image",
            "get_maps",
        )


class PropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prop
        fields = (
            "id",
            "name",
            "scene",
            "x",
            "y",
            "z",
            "max_x",
            "min_x",
            "max_y",
            "min_y",
            "max_z",
            "min_z",
            "model",
            "get_model",
        )
