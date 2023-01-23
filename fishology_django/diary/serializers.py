from rest_framework import serializers

from diary.models import Diary, Mood, Weather


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = (
            "id",
            "name",
            "icon",
        )


class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = (
            "id",
            "name",
            "icon",
            "value"
        )


class DiarySerializer(serializers.ModelSerializer):
    mood = serializers.CharField(source='mood.name')
    weather = serializers.CharField(source='weather.name')
    author = serializers.CharField(source='author.username')

    class Meta:
        model = Diary
        fields = (
            "id",
            "aquarium",
            "author",
            "fish",
            "body",
            "created",
            "mood",
            "weather",
            "get_absolute_url"
        )
