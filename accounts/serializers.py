from django.contrib.auth.models import Group, Permission

from rest_framework.serializers import HyperlinkedModelSerializer

from accounts.models import User


class PermissionSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Permission
        fields = '__all__'


class GroupSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class UserSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
