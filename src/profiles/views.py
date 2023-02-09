from rest_framework import views, mixins, viewsets, generics
from rest_framework.response import Response
from rest_framework import permissions

from utility.permissions import Owner, IsHiddenProfile
from utility.mixins import MixedActionsMixin
from .models import UserNet
from .serializer import (
    RetrieveUserNetSerializer,
    RetrieveUserNetHiddenSerializer,
    ListUserNetSerializer,
)

class UserViewSet(
    MixedActionsMixin,
    viewsets.GenericViewSet, 
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin,
    ):
    """"""
    serializers = {
        'list': ListUserNetSerializer,
        'retrieve': RetrieveUserNetSerializer,
        'update': RetrieveUserNetSerializer,
    }
    action_permissions = {
        'retrieve':[IsHiddenProfile],
        'update':[Owner]
    }

    queryset = UserNet.objects.all()

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()

    #     # Check on Hidden profile
    #     if instance.id != request.user.id and \
    #         instance.profile_is_hidden and \
    #         not instance.subscribers.filter(pk=request.user.id, relation='confirmed'):
    #         serializer = RetrieveUserNetHiddenSerializer(instance)
    #     else:
    #         serializer = self.get_serializer(instance)

    #     return Response(serializer.data)