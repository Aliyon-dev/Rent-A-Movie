from rest_framework import serializers
from .models import Genre, Movie, Customer, ZipCode


class genre_serializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre']
        
class movie_serializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
class customer_serializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        
class zipcode_serializers(serializers.ModelSerializer):
    class Meta:
        model = ZipCode
        fields = '__all__'