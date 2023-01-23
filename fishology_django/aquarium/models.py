import uuid
from django.db import models
from account.models import User
from diary.models import Diary
from scene.models import Scene, Sky
from django.db.models import Count


class Aquarium(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    host = models.ForeignKey(
        User, related_name='aquariums', on_delete=models.SET_NULL, null=True)
    participants = models.ManyToManyField(
        User, null=True, related_name="participants", blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to='uploads/aquariums/', blank=True, null=True)
    isPrivate = models.BooleanField(default=False)

    scene = models.ForeignKey(
        Scene, to_field="folder", db_column="scene", on_delete=models.CASCADE, null=True)

    sky = models.ForeignKey(Sky, to_field="folder", db_column="sky",
                            on_delete=models.CASCADE, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.id}/'

    def get_total_fish(self):
        return Diary.objects.filter(aquarium__id=self.id).count()

    def get_image(self):
        if (self.image):
            return 'http://127.0.0.1:8000' + self.image.url

        return 'http://127.0.0.1:8000' + '/media/uploads/aquariums/Aquarium_Sample.jpg'
