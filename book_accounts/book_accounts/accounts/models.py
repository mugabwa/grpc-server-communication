from django.db import models
import uuid

STATUS_CHOICES = [
        ('AVAILABLE', 'Available'),
        ('BORROWED', 'Borrowed'),
    ]

class BookAccount(models.Model):
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    book_guid = models.UUIDField()
    is_paid = models.BooleanField(default=False)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='AVAILABLE')
    borrowed_at = models.DateTimeField(null=True, blank=True)
    paid_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.book_guid

