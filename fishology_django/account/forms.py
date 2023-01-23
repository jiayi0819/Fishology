from django.forms import ModelForm
from account.models import User
import django.forms


class UserForm(ModelForm):
    image = django.forms.FileField(required=False)

    class Meta:
        model = User
        required_fields = []
        fields = [
            "username",
            "email",
            "bio",
            "birthday",
            "image"
        ]
