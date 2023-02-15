from django.db.models import Q, Count, Sum
from rest_framework import mixins, viewsets, permissions, generics
from rest_framework.response import Response

from utility.permissions import ForConfirmedSubcribers, UserIsSubscription, Owner
from utility.mixins import MixedActionsMixin, MixedPermissionMixin, MixedSerializerMixin

from . import filters
from .models import (
    UserNet,
    Follower,
    Technology,
)
from .serializer import (
    RetrieveUserSerializer,
    UserSerializer,
    FollowerSerializer,
    TechnologySerializer,
    RetrieveTechnologySerializer,
)

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    filterset_class = filters.UserFilter

    queryset = UserNet.objects.filter(profile__privacy__user_is_hidden = False)

class UserRetrieveView(generics.RetrieveAPIView):
    serializer_class = RetrieveUserSerializer
    permission_classes = [ForConfirmedSubcribers]
    queryset = UserNet.objects.all()

class FollowerViewSet(
        MixedPermissionMixin,
        viewsets.GenericViewSet,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
    ):
    action_permissions = {
        'create':[permissions.IsAuthenticated],
        'destroy':[UserIsSubscription], 
        'update':[UserIsSubscription],
    }

    filterset_class = filters.FollowerFilter
    serializer_class = FollowerSerializer

    queryset = Follower.objects.all()


### Сделать ЧЕРЕЗ ГЕТ
# class SubscribersListView(generics.ListAPIView):
#     serializer_class = FollowerSerializer
#     filterset_class = filters.FollowerFilter
#     permission_classes = [ForConfirmedSubcribers]

#     queryset = UserNet

#     def get_queryset(self):
#         user = UserNet.objects.get(pk=self.kwargs.get('pk'))
#         self.check_object_permissions(self.request, user)

#         queryset = user.subscribers.all()

#         if self.request.user != user:
#             queryset = queryset.filter(
#                 follower__profile__privacy__user_is_hidden = False,
#                 follower__profile__privacy__profile_is_hidden = False
#             )

#         return queryset

# class SubscriptionsListView(generics.ListAPIView):
#     serializer_class = FollowerSerializer
#     filterset_class = filters.FollowerFilter
#     permission_classes = [ForConfirmedSubcribers]

#     queryset = UserNet

#     def get_queryset(self):
#         user = UserNet.objects.get(pk=self.kwargs.get('pk'))
#         self.check_object_permissions(self.request, user)

#         queryset = user.subscriptions.all()

#         if self.request.user != user:
#             queryset = queryset.filter(
#                 subscription__profile__privacy__user_is_hidden = False
#             )

#         return queryset


class TechnologyViewSet(
        MixedSerializerMixin,
        viewsets.GenericViewSet,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        mixins.ListModelMixin,
    ):
    action_permissions = {
        'create':[permissions.IsAuthenticated],
        'destroy':[UserIsSubscription], 
        'update':[UserIsSubscription],
        'list':
    }

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = filters.TechnologyFilter

    lookup_field = 'url'
    lookup_url_kwarg = 'url'

    queryset = Technology.objects.filter(confirmed=True)



    filterset_class = filters.FollowerFilter
    serializer_class = FollowerSerializer

    queryset = Follower.objects.all()