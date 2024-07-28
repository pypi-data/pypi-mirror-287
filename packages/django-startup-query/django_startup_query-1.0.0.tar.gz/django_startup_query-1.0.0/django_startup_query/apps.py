from django.apps import AppConfig
from django.conf import settings
from django.db import connection

class Config(AppConfig):
    name = "django_startup_query"

    def ready(self):
        if settings.STARTUP_QUERY:
            cursor = connection.cursor()
            if settings.DEBUG:
                print(settings.STARTUP_QUERY)
            cursor.execute(settings.STARTUP_QUERY)
