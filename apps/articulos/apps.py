from django.apps import AppConfig


class ArticulosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.articulos'

    def ready(self):
        import apps.articulos.signals
