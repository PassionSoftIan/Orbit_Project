from rest_framework import serializers
from .models import *

############################################
class GenreSerializer(serializers.ModelSerializer):
    class Meta():
        model = Genre
        fields = ('name', 'id')


############################################
class Youtube_keySerializer(serializers.ModelSerializer):
    class Meta():
        model = youtube_key
        fields = ('key',)


############################################
class Still_cutSerializer(serializers.ModelSerializer):
    class Meta():
        model = stillcut
        fields = ('img_url',)
        
############################################
class ReviewSerializer(serializers.ModelSerializer):
    class Meta():
        model = Review
        fields = '__all__'

        read_only_fields = ('movie', 'user')


############################################
class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    youtube_key_set = Youtube_keySerializer(many=True, read_only=True)
    stillcut_set = Still_cutSerializer(many=True, read_only=True)

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