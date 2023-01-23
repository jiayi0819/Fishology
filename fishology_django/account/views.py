# from django.contrib.auth.models import BaseUserManager
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from account.models import User
from account.forms import UserForm
from account.serializers import UserSerializer


class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

# GET ONE USER


class UserInfo(APIView):
    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username, format=None):
        user = self.get_object(username)
        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(['POST'])
def searchUser(request, username):
    # query = request.data.get('query', '')
    query = username

    if query:
        users = User.objects.filter(username=query).exclude(
            username=request.user.username)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def updateUser(request):
    formData = UserForm(request.POST, request.FILES)
    user = User.objects.get(username=request.user.username)

    print(user.email)

    user = User(id=request.user.id, **request.data)
    user.save()

    return Response(formData.errors)
