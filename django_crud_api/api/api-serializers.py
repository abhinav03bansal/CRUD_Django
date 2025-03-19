from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Publisher

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'address')

class BookSerializer(serializers.ModelSerializer):
    publisher_name = serializers.ReadOnlyField(source='publisher.name')
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'isbn', 'publication_date', 'publisher', 'publisher_name')
