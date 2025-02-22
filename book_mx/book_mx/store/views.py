from rest_framework import viewsets

from book_mx.store.models import Book, BookStore
from book_mx.store.serializer import BookSerializer, BookStoreSerializer


class BookStoreViewSet(viewsets.ModelViewSet):
    queryset = BookStore.objects.all()
    serializer_class = BookStoreSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
