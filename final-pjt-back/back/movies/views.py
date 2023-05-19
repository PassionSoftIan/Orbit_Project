from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

######################################################################
@api_view(['GET'])
def get_movie_title(request):
    movies = Movie.objects.filter(title__in=list(request.GET))
    serializer = MovieSerializer(movies, many=True)

    return Response(serializer.data)
    

######################################################################
@api_view(['GET'])
def get_movie_all_title(request):
    movies = Movie.objects.all()
    serializer = MovietitleSerializer(movies, many=True)

    return Response(serializer.data)


######################################################################
@api_view(['GET'])
def get_movie(request):
    try:
        page = int(request.GET['page'])
    except:
        return Response({'page' : "this key is required or need to int"}, status=400)
    try:
        sort_key = "-" + request.GET['order_by']
    except KeyError:
        sort_key = '-vote_average'

    try:
        genre = request.GET['genre']
        movies = Movie.objects.filter(genre = genre).order_by(sort_key)[:100]
    except KeyError:
        print(sort_key)
        movies = Movie.objects.all()
    # movies = Movie.objects.all()[page*10:page*10+10]
    serializers = MovieSerializer(movies, many=True)

    return Response(serializers.data)


######################################################################
@api_view(['GET', 'PUT'])
def get_movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=200)
    
    if request.method == "PUT":
        serializer = MoviepopularitySerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(MovieSerializer(movie).data)
    

######################################################################
@api_view(['GET', 'POST'])
def review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == "GET":
        reviews = movie.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=201)
        

######################################################################
@api_view(['PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.user != request.user:
        return Response({"message":"User isn't authenticated"}, status=401)

    if request.method == "PUT":
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    
    if request.method == "DELETE":
        review.delete()
        return Response({"message":"clear delete"}, status=204)


######################################################################
@api_view(['GET'])
def genre_list(request):
    genre = Genre.objects.all()
    serializer = GenreSerializer(genre, many=True)

    return Response(serializer.data)



######################################################################
def api_list(request):
    return render(request, 'movies/apilist.html')
    

