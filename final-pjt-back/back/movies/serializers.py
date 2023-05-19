from rest_framework import serializers
from .models import *

############################################
class GenreSerializer(serializers.ModelSerializer):
    class Meta():
        model = Genre
        fields = ('name', 'id')


############################################
class ReviewSerializer(serializers.ModelSerializer):
    class Meta():
        model = Review
        fields = '__all__'

        read_only_fields = ('movie', 'user')


############################################
class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)

    class Meta():
        model = Movie
        fields = '__all__'
        

############################################
class MoviepopularitySerializer(serializers.ModelSerializer):
    class Meta():
        model = Movie
        fields = ('popularity',)


############################################
class MovietitleSerializer(serializers.ModelSerializer):
    class Meta():
        model = Movie
        fields = ('id', 'title')