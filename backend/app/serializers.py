from rest_framework import serializers
from app.models import BookStoreModel
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookStoreModel
        fields = '__all__'