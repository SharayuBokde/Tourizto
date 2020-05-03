from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'Accounts'

    def ready(self):
        import Accounts.signals
