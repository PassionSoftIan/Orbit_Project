from rest_framework import serializers
from .models import *

from accounts.models import User
from django.conf import settings


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
class userSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ('id', 'nick_name')

############################################
class ReviewSerializer(serializers.ModelSerializer):
    # user = userSerializer(read_only=True)
    class Meta():
        model = Review
        fields = '__all__'

        read_only_fields = ('movie', 'user')


############################################
class ReviewReadSerializer(serializers.ModelSerializer):
    user = userSerializer(read_only=True)
    class Meta():
        model = Review
        fields = '__all__'

        read_only_fields = ('movie', )
        

############################################
class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    youtube_key_set = Youtube_keySerializer(many=True, read_only=True)
    stillcut_set = Still_cutSerializer(many=True, read_only=True)
    genre_annotation = GenreSerializer(many=True, read_only=True)
    

    class Meta():
        model = Movie
        fields = '__all__'

    def get_genre(self,obj):
        if obj.genre_annotation:
            return obj.genre_annotation
        return
        

############################################
class MoviepopularitySerializer(serializers.ModelSerializer):
    class Meta():
        model = Movie
        fields = ('popularity',)


############################################
class MovietitleSerializer(serializers.ModelSerializer):
    class Meta():
        model = Movie
        # 기존 fields(id, title) 에 'revenue','vote_average','poster_path' 추가(세울!)
        fields = ('id', 'title','revenue','vote_average','poster_path')