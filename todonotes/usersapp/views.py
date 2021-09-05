from rest_framework import mixins, viewsets
from usersapp.models import MyUsersModel
from usersapp.serializers import UserSerializer


class UsersModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = MyUsersModel.objects.all()
