from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "backups_operator.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import backups_operator.users.signals  # noqa F401
        except ImportError:
            pass
