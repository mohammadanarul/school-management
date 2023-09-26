from apps.libraries.models import Library, Book
from rest_framework import serializers


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
