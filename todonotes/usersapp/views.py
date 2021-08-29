from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .models import MyUsersModel
from .serializers import UserSerializer


class UsersModelViewSet(ModelViewSet):
    queryset = MyUsersModel.objects.all()
    serializer_class = UserSerializer
