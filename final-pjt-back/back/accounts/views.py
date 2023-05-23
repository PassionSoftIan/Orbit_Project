from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from movies.models import Review
from .serializers import *

# Create your views here.
# 기존 view를 바꿔 코인 업데이트 될 수 있게 수정(인식)
@api_view(['GET', 'PUT'])
def get_user(request, user_pk):
    user = get_object_or_404(User, pk = user_pk)
    if request.method == "GET":
        # reviews = user.review_set.all()
        # serializer = ReviewSerializer(reviews, many=True)
        # return Response(serializer.data)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        coins = request.data.get('coins')
        user.coins += int(coins)
        user.save()
        return Response({'message': 'Coins updated successfully'})

@api_view(['POST', 'DELETE'])
def following(request, user_pk):
    follower = get_object_or_404(User, pk = user_pk)

    if request.method == "POST":
        if request.user in follower.followers.all():
            return Response({"message": "now following"}, status=400)
        else:
            follower.followers.add(request.user)
            return Response({"message": "following"}, status=201)

    elif request.method == "DELETE":
        if request.user in follower.followers.all():
            follower.followers.remove(request.user)
            return Response({"message": "delete"}, status=201)
        else:
            return Response({"message": "not follow"}, status=400)


@api_view(['POST', 'DELETE'])
def like_reviews(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)

    if request.method == "POST":
        if request.user in review.liked_user.all():
            return Response({"message":"now liked"}, status=400)
        else:
            review.liked_user.add(request.user)
            return Response({"message": "like"}, status=201)


    elif request.method == "DELETE":
        if request.user in review.liked_user.all():
            review.liked_user.remove(request.user)
            return Response({"message": "unlike"}, status=201)
        else:
            return Response({"message": "dont like"}, status=400)


