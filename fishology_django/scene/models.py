import uuid
from django.db import models


class Scene(models.Model):
    # id = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=True)
    folder = models.CharField(unique=True, max_length=200, null=True)
    name = models.CharField(unique=True, max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to='uploads/aquariums/', blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_image(self):
        if (self.image):
            return 'http://127.0.0.1:8000' + self.image.url


class Sky(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to='uploads/skies/', blank=True, null=True)
    folder = models.CharField(
        primary_key=True, unique=True, max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_image(self):
        if (self.image):
            return 'http://127.0.0.1:8000' + self.image.url

    def get_maps(self):
        return 'http://127.0.0.1:8000' + '/media/models/sky/' + self.folder


class Prop(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    scene = models.ForeignKey(
        Scene, on_delete=models.CASCADE, to_field='folder', null=True)

    x = models.DecimalField(max_digits=30, decimal_places=2)
    y = models.DecimalField(max_digits=30, decimal_places=2)
    z = models.DecimalField(max_digits=30, decimal_places=2)

    max_x = models.DecimalField(max_digits=30, decimal_places=2)
    min_x = models.DecimalField(max_digits=30, decimal_places=2)
    max_y = models.DecimalField(max_digits=30, decimal_places=2)
    min_y = models.DecimalField(max_digits=30, decimal_places=2)
    max_z = models.DecimalField(max_digits=30, decimal_places=2)
    min_z = models.DecimalField(max_digits=30, decimal_places=2)

    model = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_model(self):
        return 'http://127.0.0.1:8000/media/models/aquarium/' + str(self.scene.folder) + '/' + self.model + '.glb'
