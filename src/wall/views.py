from rest_framework import mixins, viewsets, permissions

from profiles.models import UserNet
from utility.permissions import IsHiddenProfile
from wall.serializers import ListPostSerialier, RetrievePostSerializer
from wall.models import (
    Post,
    PostComment,
    PostReaction,
    CommentReaction,
)


class WallView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = ListPostSerialier

    permission_classes = [
        permissions.IsAuthenticated,
    ]
    
    def get_queryset(self):
        queryset = Post.objects.filter(
            published=True,
            user__id__in = self.request.user.subscriptions.all().values('subscription__id')
        ).order_by('-published_date')
        return queryset