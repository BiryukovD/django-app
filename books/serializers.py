# serializers.py
from rest_framework import serializers
from .models import Book 

class BookSerializer(serializers.ModelSerializer):
    # Определите, как данные модели Book будут сериализованы
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

    # def create(self, validated_data):
    #     book = Book(
    #         title=validated_data['title'],
    #         author=validated_data['author'],
    #         published_date=validated_data['published_date']
    #     )
    #     return book    
        # Если вы хотите исключить поле user из сериализованного вывода, можно сделать это:
        # exclude = ['user']
