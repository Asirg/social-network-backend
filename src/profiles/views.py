from rest_framework import views, mixins, viewsets, generics
from rest_framework.response import Response
from rest_framework import permissions

from .permissions import Owner
from .models import UserNet
from .serializer import (
    RetrieveUserNetSerializer,
    ListUserNetSerializer,
    CreateUserNetSerializer
)


class UserPublicView(viewsets.ReadOnlyModelViewSet):
    """"""
    queryset = UserNet.objects.all()
    serializer_class = RetrieveUserNetSerializer
    permission_classes = [permissions.AllowAny]

class UserViewSet(viewsets.ModelViewSet):
    """"""
    serializers = {
        'list': ListUserNetSerializer,
        'retrieve': RetrieveUserNetSerializer,
        'update': RetrieveUserNetSerializer,
        'create':CreateUserNetSerializer
    }
    queryset = UserNet.objects.all()

    permission_classes = [
        Owner,
        permissions.IsAuthenticated
    ]
    def get_serializer_class(self, *args, **kwargs):
        return self.serializers.get(self.action)