
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from fish.models import Fish
from fish.serializers import FishSerializer


class FishList(APIView):
    def get(self, request, format=None):
        fishes = Fish.objects.all().order_by('price')
        serializer = FishSerializer(fishes, many=True)
        return Response(serializer.data)


class FishInfo(APIView):
    def get_object(self, fish_id):
        try:
            return Fish.objects.get(id=fish_id)
        except Fish.DoesNotExist:
            raise Http404

    def get(self, request, fish_id, format=None):
        fish = self.get_object(fish_id)
        serializer = FishSerializer(fish)
        return Response(serializer.data)
