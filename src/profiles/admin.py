from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from profiles.models import (
    UserNet,
    UserAvatar,
    SocialContacts,
    UserContacts,
    Technology,
    UserTechnology
)

class UserAdminNet(UserAdmin):
    list_display = ("id", "username", "email", "first_name", "last_name", "is_staff")
    list_display_links = ('username', )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "middle_name", "gender", "birthday", "email")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(UserNet, UserAdminNet)

admin.site.register(UserAvatar)
admin.site.register(SocialContacts)
admin.site.register(UserContacts)
admin.site.register(Technology)
admin.site.register(UserTechnology)