from django.forms import ModelForm
from aquarium.models import Aquarium


class AquariumForm(ModelForm):

    class Meta:
        model = Aquarium
        required_fields = []
        fields = [
            "name",
            "description",
            "participants",
            "isPrivate",
        ]
