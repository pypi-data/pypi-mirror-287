from django.apps import AppConfig
from django.conf import settings
from django.core.management import call_command

class Config(AppConfig):
    name = "django_startup_command"

    def ready(self):
        if settings.STARTUP_COMMAND:
            call_command(settings.STARTUP_COMMAND)
