from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from todoapp.models import ProjectModel, NoteModel
from todoapp.serializers import ProjectModelSerializer, NoteModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectModelSerializer


class NoteModelViewSet(ModelViewSet):
    queryset = NoteModel.objects.all()
    serializer_class = NoteModelSerializer




