from rest_framework import serializers
from .models import Genre


class genre_serializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre']
