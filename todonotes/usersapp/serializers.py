from rest_framework.serializers import HyperlinkedModelSerializer
from .models import MyUsersModel


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = MyUsersModel
        fields = ['username', 'first_name', 'last_name', 'email']
