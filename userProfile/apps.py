from django.apps import AppConfig


class UserprofileConfig(AppConfig):
    name = 'userProfile'

    def ready(self):
        import userProfile.signals