from rest_framework import views, mixins, viewsets, generics
from rest_framework.response import Response
from rest_framework import permissions

from utility.permissions import Owner, ForConfirmedSubcribers
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
    # mixins.ListModelMixin, 
    mixins.RetrieveModelMixin, 
    # mixins.UpdateModelMixin,
    ):
    """"""
    serializers = {
        # 'list': ListUserNetSerializer,
        'retrieve': RetrieveUserNetSerializer,
        # 'update': RetrieveUserNetSerializer,
    }
    action_permissions = {
        'retrieve':[ForConfirmedSubcribers],
        'update':[Owner]
    }

    queryset = UserNet.objects.all()