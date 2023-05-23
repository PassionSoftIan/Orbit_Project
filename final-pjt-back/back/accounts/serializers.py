from rest_framework import serializers
from .models import *
from movies.serializers import ReviewSerializer, ReviewReadSerializer

####################################################################
class User_nick_name_Serializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ("nick_name", "id")


####################################################################
class UserSerializer(serializers.ModelSerializer):
    myreviews = ReviewSerializer(many = True, read_only=True)
    followings = User_nick_name_Serializer(many = True, read_only=True)
    followers = User_nick_name_Serializer(many = True, read_only=True)
    like_reveiw = ReviewReadSerializer(many = True, read_only=True)

    class Meta():
        model = User
        fields = ('username', 'nick_name', 'id', 'myreviews', "followings", "followers", "like_reveiw")
        # fields = "__all__"