from django.apps import AppConfig


class BoardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'boards'

class MeasurementsConfig(AppConfig):
    name = 'measurements'
    verbose_name = 'Measurement between 2 locations'