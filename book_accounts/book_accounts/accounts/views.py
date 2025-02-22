from book_accounts.accounts.models import BookAccount
from book_accounts.accounts.serializer import BookAccountSerializer
from rest_framework import viewsets

class BookAccountViewSet(viewsets.ModelViewSet):
    queryset = BookAccount.objects.all()
    serializer_class = BookAccountSerializer
