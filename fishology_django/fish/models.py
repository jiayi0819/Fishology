import uuid
from django.db import models


class Fish(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/fish/', blank=True, null=True)
    model = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_image(self):
        if (self.image):
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_lock_image(self):
        return 'http://127.0.0.1:8000' + '/media/uploads/fish/unknown.svg'

    def get_model(self):
        return 'http://127.0.0.1:8000/media/models/fish/' + self.model + '.glb'
