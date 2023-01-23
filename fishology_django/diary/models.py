import uuid
from django.db import models
### from django.contrib.auth.models import User

# from aquarium.models import Aquarium
from account.models import User
from fish.models import Fish


class Weather(models.Model):
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Mood(models.Model):
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    value = models.IntegerField()

    def __str__(self):
        return self.name


class Diary(models.Model):
    # author =
    # tag =

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(
        User, related_name='diaries', on_delete=models.SET_NULL, null=True)
    aquarium = models.ForeignKey(
        'aquarium.Aquarium', related_name="diaries", on_delete=models.CASCADE, default=None)
    fish = models.ForeignKey(
        Fish, related_name="diaries", on_delete=models.CASCADE, default=None)

    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
    weather = models.ForeignKey(Weather, on_delete=models.CASCADE)

    def __str__(self):
        return self.body[0:50]

    def get_absolute_url(self):
        return f'/{self.id}/'
