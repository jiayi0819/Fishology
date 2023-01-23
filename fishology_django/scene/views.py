from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from scene.models import Prop, Scene, Sky
from scene.serializers import PropSerializer, SceneSerializer, SkySerializer


class PropList(APIView):
    def get_object(self, scene_name):
        try:
            return Prop.objects.filter(scene__folder=scene_name)
        except Prop.DoesNotExist:
            raise Http404

    def get(self, request, scene_name, format=None):
        props = self.get_object(scene_name)
        serializer = PropSerializer(props, many=True)
        return Response(serializer.data)


class SceneList(APIView):
    def get(self, request, format=None):
        scenes = Scene.objects.all()
        serializer = SceneSerializer(scenes, many=True)
        return Response(serializer.data)


class SkyList(APIView):
    def get(self, request, format=None):
        skies = Sky.objects.all()
        serializer = SkySerializer(skies, many=True)
        return Response(serializer.data)
