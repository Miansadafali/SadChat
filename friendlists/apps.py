from django.apps import AppConfig


class FriendlistsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'friendlists'
    
    def ready(self):
        import friendlists.signals
