from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book_accounts.accounts'

    def ready(self):
        import book_accounts.accounts.signals
