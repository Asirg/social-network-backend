from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from profiles.models import (
    UserNet,
    UserAvatar,
    UserContacts,
    Technology,
    UserTechnology,
    Follower,
    Profile,
    PrivacySettings,
)

admin.site.register(UserNet, UserAdmin)
admin.site.register(Follower)

admin.site.register(Profile)
admin.site.register(PrivacySettings)
admin.site.register(UserAvatar)
admin.site.register(UserContacts)
admin.site.register(Technology)
admin.site.register(UserTechnology)