from django.apps import AppConfig


class RedisIntroConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "redis_intro"

    def ready(self):
        from . import signals
