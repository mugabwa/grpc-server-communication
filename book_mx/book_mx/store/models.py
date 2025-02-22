from django.db import models
import uuid

STATUS_CHOICES = [
        ('AVAILABLE', 'Available'),
        ('BORROWED', 'Borrowed'),
    ]

class BookStore(models.Model):
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=20)
    store = models.ForeignKey(BookStore, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='AVAILABLE')
