from rest_framework import serializers
from .models import Genre, Movie


class genre_serializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre']
        
class movie_serializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'