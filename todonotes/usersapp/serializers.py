from rest_framework.serializers import HyperlinkedModelSerializer, Serializer, ModelSerializer
from usersapp.models import MyUsersModel


class UserSerializer(ModelSerializer):
    class Meta:
        model = MyUsersModel
        fields = ('username', 'first_name', 'last_name', 'email')
