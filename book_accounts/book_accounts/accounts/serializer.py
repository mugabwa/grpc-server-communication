from book_accounts.accounts.models import BookAccount
from rest_framework import serializers

class BookAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAccount
        fields = '__all__'
