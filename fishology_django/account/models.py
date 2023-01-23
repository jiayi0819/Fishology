from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# from account.views import UserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, **other_fields):

        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        user = self.create_user(email, password, **other_fields)
        user.is_active = True
        user.save()
        return user


class User(AbstractUser):
    # username = None
    # name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    birthday = models.DateField(null=True)

    image = models.ImageField(
        upload_to='uploads/user/', blank=True, null=True)

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_image(self):
        if (self.image):
            return 'http://127.0.0.1:8000' + self.image.url
        return 'http://127.0.0.1:8000' + '/media/uploads/user/avatar.svg'
