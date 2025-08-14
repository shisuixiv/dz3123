from rest_framework import serializers

from .models import Library, Book

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['id', 'title', 'description', 'image']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','date','author']