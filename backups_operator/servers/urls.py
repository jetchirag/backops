from django.urls import path

import backups_operator.servers.views as Views

app_name = "servers"
urlpatterns = [
    path("test/", view=Views.test, name="redirect"),
    path("auth/", view=Views.authHome, name="authHome"),
    path("<int:id>", view=Views.manage, name="manage"),
    path("", view=Views.home, name="home"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
