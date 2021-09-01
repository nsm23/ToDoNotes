from rest_framework.relations import StringRelatedField
from rest_framework.serializers import Serializer

from todoapp.models import ProjectModel, NoteModel
from usersapp.serializers import UserSerializer


class ProjectModelSerializer(Serializer):
    author = UserSerializer

    class Meta:
        model = ProjectModel
        fields = '__all__'


class NoteModelSerializer(Serializer):
    authors = StringRelatedField(many=True)

    class Meta:
        model = NoteModel
        fields = '__all__'
