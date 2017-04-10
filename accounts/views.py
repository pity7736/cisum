from django.contrib.auth.models import Group, Permission

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from accounts.serializers import UserSerializer, GroupSerializer, PermissionSerializer
from accounts.models import User


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PermissionViewSet(ReadOnlyModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
