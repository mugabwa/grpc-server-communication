from django.db.models.signals import post_save
from django.dispatch import receiver
from book_accounts.accounts.models import BookAccount

from book_accounts.accounts.grpc_client import send_event

@receiver(post_save, sender=BookAccount)
def notify_book_mx_change(sender, instance, **kwargs):
    send_event('book_account_status_changed', instance.status, str(instance.book_guid))
    print('Book account status changed:', instance.status)
