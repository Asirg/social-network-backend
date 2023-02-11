from rest_framework.permissions import BasePermission


SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class Owner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id  == obj.id

class ForConfirmedSubcribers(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user.id  == obj.id or
            not obj.profile_is_hidden or
            obj.subscribers.filter(follower__id=request.user.id, relation='confirmed')
        )

    # user_is_hiden = models.BooleanField(default=False) # Hidden user everywhere
    # profile_is_hidden = models.BooleanField(default=False) # Hidden information on user profile
    # chat_is_closed = models.CharField(max_length=20, choices=HIDDEN_STATUS, default='all') # Close send message
    # activity_status_is_hidden = models.CharField(max_length=20, choices=HIDDEN_STATUS, default='all') # Hidden current status and time last login 