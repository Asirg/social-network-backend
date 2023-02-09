class MixedSerializerMixin:

    def get_serializer_class(self, *args, **kwargs):
        return self.serializers.get(self.action)

class MixedPermissionMixin:
    def get_permissions(self):
        try:
            return [permission() for permission in self.action_permissions.get(self.action)]
        except:
            return [permission() for permission in self.permission_classes]

class MixedActionsMixin(MixedSerializerMixin, MixedPermissionMixin):
    pass
