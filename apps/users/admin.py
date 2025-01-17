from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .forms import GroupAdminForm, UserAdminForm
from .models import ProxyGroup

User = get_user_model()


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    form = UserAdminForm
    list_display = (
        "username",
        "is_active",
        "role",
    )
    list_filter = (
        "email",
        "username",
    )

    def get_readonly_fields(self, request, obj=None):
        """Only superusers can edit `is_superuser` field."""
        if not request.user.is_superuser:
            return ("is_superuser",)
        return super().get_readonly_fields(request, obj)

    @admin.display(description="Роль")
    def role(self, obj):
        return obj.groups.first()


class GroupAdmin(admin.ModelAdmin):

    form = GroupAdminForm
    list_display = ["name"]
    filter_horizontal = ("permissions",)


admin.site.register(ProxyGroup, GroupAdmin)
