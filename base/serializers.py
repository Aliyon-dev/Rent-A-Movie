from rest_framework import serializers
from .models import Genre, Movie, Customer, ZipCode, Rental


class genre_serializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']
        
class movie_serializer(serializers.ModelSerializer):
    genre = genre_serializer()
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
class rental_serializers(serializers.ModelSerializer):
    customer = customer_serializers()
    movie  = movie_serializer()
    
    class Meta:
         model = Rental
         fields = '__all__'