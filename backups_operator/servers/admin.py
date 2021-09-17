from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from backups_operator.servers.models import Server, AuthData

admin.site.register(Server)
admin.site.register(AuthData)

# @admin.register(Server)
# class ServerAdmin(admin):
#     pass

    # form = UserChangeForm
    # add_form = UserCreationForm
    # fieldsets = (
    #     (None, {"fields": ("username", "password")}),
    #     (_("Personal info"), {"fields": ("name", "email")}),
    #     (
    #         _("Permissions"),
    #         {
    #             "fields": (
    #                 "is_active",
    #                 "is_staff",
    #                 "is_superuser",
    #                 "groups",
    #                 "user_permissions",
    #             ),
    #         },
    #     ),
    #     (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    # )
    # list_display = ["username", "name", "is_superuser"]
    # search_fields = ["name"]
