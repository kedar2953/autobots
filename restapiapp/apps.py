from django.apps import AppConfig


class RestapiappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restapiapp'

    def ready(self) :
        from restapiapp import updater
        updater.start()