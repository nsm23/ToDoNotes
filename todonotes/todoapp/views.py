from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from todoapp.filters import NotesFilter
from todoapp.models import ProjectModel, NoteModel
from todoapp.paginations import ProjectPagination, NotesPagination
from todoapp.serializers import ProjectModelSerializer, NoteModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectPagination


class NoteModelViewSet(ModelViewSet):
    queryset = NoteModel.objects.all()
    serializer_class = NoteModelSerializer
    pagination_class = NotesPagination
    filter_class = NotesFilter

    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)





