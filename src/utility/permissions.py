from rest_framework.permissions import BasePermission
from .services import check_user_privacy


SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class Owner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id  == obj.id

class UserIsSubscription(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id  == obj.subscription.id

# class IsHiddenProfile(BasePermission):

class ForConfirmedSubcribers(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            not obj.profile.privacy.profile_is_hidden or
            check_user_privacy(obj, request.user) != 'all'
        )