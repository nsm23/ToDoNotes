from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from usersapp.models import MyUsersModel
from usersapp.serializers import UserSerializer


class UsersModelViewSet(ModelViewSet):
    queryset = MyUsersModel.objects.all()
    serializer_class = UserSerializer
