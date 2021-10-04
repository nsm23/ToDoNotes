from graphene import Schema, ObjectType, List, Int, ID, String, Field
from graphene_django import DjangoObjectType

from todoapp.models import ProjectModel, NoteModel
from usersapp.models import MyUsersModel


class ProjectDjangoType(DjangoObjectType):
    class Meta:
        model = ProjectModel
        fields = '__all__'


class UsersDjangoType(DjangoObjectType):
    class Meta:
        model = MyUsersModel
        fields ='__all__'


class NoteDjangoType(DjangoObjectType):
    class Meta:
        model = NoteModel
        fields = '__all__'


class Query(ObjectType):
    all_projects = List(ProjectDjangoType)
    all_users = List(UsersDjangoType)
    all_notes = List(NoteDjangoType)

    def resolve_all_projects(self, info):
        return ProjectModel.objects.all()

    def resolve_all_users(self, info):
        return MyUsersModel.objects.all()

    def resolve_all_notes(self, info):
        return NoteModel.objects.all()



schema = Schema(query=Query)


