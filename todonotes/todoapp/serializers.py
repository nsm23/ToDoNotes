from django.db.migrations import serializer
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from todoapp.models import ProjectModel, NoteModel
from usersapp.serializers import UserSerializer


class ProjectModelSerializer(ModelSerializer):
    author = UserSerializer

    class Meta:
        model = ProjectModel
        fields = '__all__'


class NoteModelSerializer(ModelSerializer):
    authors = StringRelatedField(many=True)

    class Meta:
        model = NoteModel
        fields = '__all__'
