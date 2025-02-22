from book_mx.store.models import Book, BookStore
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookStore
        fields = '__all__'