from django.apps import AppConfig
import home 

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
def ready(self):
    import myapp.signals
