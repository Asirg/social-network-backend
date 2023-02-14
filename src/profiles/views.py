from rest_framework import mixins, viewsets, permissions
from django.views import generic

from utility.permissions import ForConfirmedSubcribers, UserIsSubscription, Owner
from utility.mixins import MixedActionsMixin, MixedPermissionMixin, MixedSerializerMixin
from . import filters
from .models import (
    UserNet,
    Follower,
    Technology,
    UserContacts,
    UserTechnology
)
from .serializer import (
    RetrieveUserSerializer,
    UpdateUserSerializer,
    UserSerializer,
    FollowerSerializer,
    TechnologySerializer,
    RetrieveTechnologySerializer,
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
        'list': UserSerializer,
        'retrieve': RetrieveUserSerializer,
        'update': UpdateUserSerializer,
    }
    action_permissions = {
        'retrieve':[ForConfirmedSubcribers],
        'update':[permissions.AllowAny],
    }

    filterset_class = filters.UserFilter

    queryset = UserNet.objects.all()
class FollowerViewSet(
        MixedPermissionMixin,
        viewsets.GenericViewSet,
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
    ):
    action_permissions = {
        'destroy':[UserIsSubscription], 
        'update':[UserIsSubscription],
    }

    filterset_class = filters.FollowerFilter
    serializer_class = FollowerSerializer

    queryset = Follower.objects.all()

class TechnologyViewSet(
        MixedSerializerMixin,
        viewsets.GenericViewSet,
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
    ):
    serializers = {
        'list': TechnologySerializer,
        'retrieve': RetrieveTechnologySerializer,
        'create': RetrieveTechnologySerializer,
    }
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = filters.TechnologyFilter

    lookup_field = 'url'
    lookup_url_kwarg = 'url'

    queryset = Technology.objects.filter(confirmed=True)