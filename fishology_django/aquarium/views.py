from django.db.models import Q
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from account.models import User
from scene.models import Sky, Scene

from aquarium.models import Aquarium
from aquarium.serializers import AquariumSerializer


class AquariumList(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        aquariums = Aquarium.objects.filter(
            Q(participants=request.user) | Q(host=request.user.id))
    # def get(self, request, user_name, format=None):
    #     print(user_name)
    #     aquariums = Aquarium.objects.filter(
    #         Q(participants=user_name) | Q(host=user_name))
        serializer = AquariumSerializer(aquariums, many=True)
        return Response(serializer.data)


class AquariumInfo(APIView):

    def get_object(self, aquarium_id):
        try:
            return Aquarium.objects.get(id=aquarium_id)
        except Aquarium.DoesNotExist:
            raise Http404

    def get(self, request, aquarium_id, format=None):
        aquarium = self.get_object(aquarium_id)
        serializer = AquariumSerializer(aquarium)
        return Response(serializer.data)


@api_view(['POST'])
def createAquarium(request):
    users = []
    participants = request.data.pop('participants')
    print(participants)

    for participant in participants:
        try:
            user = User.objects.get(username=participant)
            users.append(user)
        except ObjectDoesNotExist:
            raise Http404

    aquarium = Aquarium()
    aquarium = Aquarium.objects.create(
        host=request.user, **request.data)
    aquarium.participants.set(users)
    aquarium.save()

    return Response(AquariumSerializer(aquarium).data)


@api_view(['POST'])
def updateAquariumSky(request, aquarium_id, sky_name):
    try:
        aquarium = Aquarium.objects.get(id=aquarium_id)
    except Aquarium.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        aquarium.sky = Sky.objects.get(folder=sky_name)
        aquarium.save()
        return Response(AquariumSerializer(aquarium).data)


@api_view(['POST'])
def updateAquariumScene(request, aquarium_id, scene_name):
    try:
        aquarium = Aquarium.objects.get(id=aquarium_id)
    except Aquarium.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        aquarium.scene = Scene.objects.get(folder=scene_name)
        aquarium.save()
        return Response(AquariumSerializer(aquarium).data)


@api_view(['POST', 'DELETE'])
def updateAquarium(request, aquarium_id):

    print(aquarium_id)

    try:
        aquarium = Aquarium.objects.get(id=aquarium_id)
    except Aquarium.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':

        # DEAL WITH PARTICIPANTS
        participants = []

        # CLEAN PARTICIPANT DATA
        users = request.data.pop('participants')

        for user in users:
            print(user)
            try:
                participant = User.objects.get(username=user)
                participants.append(participant)
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        request.data.pop('get_absolute_url')
        request.data.pop('get_image')
        request.data.pop('host')
        # host = User(request.data.pop('host'))

        # aquarium = Aquarium(**request.data)
        aquarium.name = request.data['name']
        aquarium.description = request.data['description']
        aquarium.isPrivate = request.data['isPrivate']
        aquarium.participants.set(participants)
        aquarium.save()

        return Response(AquariumSerializer(aquarium).data)

    elif request.method == 'DELETE':
        aquarium.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
