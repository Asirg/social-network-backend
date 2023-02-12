from rest_framework.permissions import BasePermission


SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class Owner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id  == obj.id

class UserIsSubscription(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id  == obj.subscription.id

class ForConfirmedSubcribers(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user.id  == obj.id or
            not obj.profile_is_hidden or
            obj.subscribers.filter(follower__id=request.user.id, relation='confirmed')
        )