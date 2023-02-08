from rest_framework.permissions import BasePermission



SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class Owner(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or 
            request.user.id  == view.get_object().id
        )