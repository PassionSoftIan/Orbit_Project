from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from django.db.models import F,Value,ExpressionWrapper

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

    genre_list = [('12','모험'),
                    ('14',    '판타지'),
                    ('16',    '애니메이션'),
                    ('18',    '드라마'),
                    ('27',    '공포'),
                    ('28',    '액션'),
                    ('35',    '코미디'),
                    ('36',    '역사'),
                    ('37',    '서부'),
                    ('53',    '스릴러'),
                    ('80',    '범죄'),
                    ('99',    '다큐멘터리'),
                    ('878',    'SF'),
                    ('9648',    '미스터리'),
                    ('10402',    '음악'),
                    ('10749',    '로맨스'),
                    ('10751',    '가족'),
                    ('10752',    '전쟁'),]

    movies = {}
    movie = Movie.objects.filter(revenue__gte = 10000).order_by(sort_key)[page*20:page*20+20]
    movies['Top20'] = MovieSerializer(movie, many=True).data
    movie = Movie.objects.filter(revenue__gte = 10000).order_by('-revenue')[page*20:page*20+20]

    ################################### 잠시 로딩 시간이 길어질 것 같아서 이쪽만 주석 처리함

    # movies['수익'] = MovieSerializer(movie, many=True).data
    # for id, genre in genre_list:
    #     movie = Movie.objects.filter(genre = id).filter(revenue__gte = 10000).order_by(sort_key)[:100]
    #     movies[genre] = MovieSerializer(movie, many=True).data
    # serializers = MovieSerializer(movies, many=True)

    return Response(movies)
#############################################################################################################
    # try:
    #     genre_list = [('12','모험'),
    #                 ('14',	'판타지'),
    #                 ('16',	'애니메이션'),
    #                 ('18',	'드라마'),
    #                 ('27',	'공포'),
    #                 ('28',	'액션'),
    #                 ('35',	'코미디'),
    #                 ('36',	'역사'),
    #                 ('37',	'서부'),
    #                 ('53',	'스릴러'),
    #                 ('80',	'범죄'),
    #                 ('99',	'다큐멘터리'),
    #                 ('878',	'SF'),
    #                 ('9648',	'미스터리'),
    #                 ('10402',	'음악'),
    #                 ('10749',	'로맨스'),
    #                 ('10751',	'가족'),
    #                 ('10752',	'전쟁'),]
    #     test = request.GET['genre']
    #     movies = {}
    #     for genre,name in genre_list:
    #         movie = Movie.objects.filter(genre = genre).filter(revenue__gte = 50).order_by(sort_key)[:100].annotate(genre_annotation=Value(name,output_field=models.CharField(max_length=50)))
    #         movies[name] = MovieSerializer(movie,many=True).data
    #     return Response(movies)
        
        
    # except KeyError:
    #     movies = Movie.objects.filter(revenue__gte = 10000).order_by(sort_key)[page*20:page*20+20]
    # # movies = Movie.objects.all()[page*10:page*10+10]
    # serializers = MovieSerializer(movies, many=True)
    
    # return Response(serializers.data)



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
        serializer = ReviewReadSerializer(reviews, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = ReviewSerializer(data=request.data)
        print("당연히 여긴 오고")
        if serializer.is_valid(raise_exception=True):
            vote_serializer = MoviepopularitySerializer(movie)
            save_vote = vote_serializer.data['ours_vote'] + float(request.data['vote'])
            save_vote_count = vote_serializer.data['vote_count'] + 1
            vote_serializer = MoviepopularitySerializer(movie, data={'ours_vote': save_vote, 'vote_count': save_vote_count})
            if vote_serializer.is_valid(raise_exception=True):
                vote_serializer.save()

            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=201)
        

######################################################################
@api_view(['PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.user != request.user:
        return Response({"message":"User isn't authenticated"}, status=401)



    if request.method == "PUT":
        serializer = ReviewSerializer(review)
        movie = Movie.objects.get(pk = serializer.data['movie'])
        before_vote = serializer.data['vote']
        vote_serializer = MoviepopularitySerializer(movie)
        save_vote = vote_serializer.data['ours_vote'] + float(request.data['vote']) - before_vote
        save_vote_count = vote_serializer.data['vote_count']
        vote_serializer = MoviepopularitySerializer(movie, data={'ours_vote': save_vote, 'vote_count': save_vote_count})
        if vote_serializer.is_valid(raise_exception=True):
            vote_serializer.save()

        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


        return Response(serializer.data)
    
    if request.method == "DELETE":
        serializer = ReviewSerializer(review)
        movie = Movie.objects.get(pk = serializer.data['movie'])
        before_vote = serializer.data['vote']
        vote_serializer = MoviepopularitySerializer(movie)
        save_vote = vote_serializer.data['ours_vote'] - before_vote
        save_vote_count = vote_serializer.data['vote_count'] - 1
        vote_serializer = MoviepopularitySerializer(movie, data={'ours_vote': save_vote, 'vote_count': save_vote_count})
        if vote_serializer.is_valid(raise_exception=True):
            vote_serializer.save()
        review.delete()
        return Response({"message":"clear delete"}, status=204)


######################################################################
@api_view(['GET'])
def genre_list(request):
    genre = Genre.objects.all()
    serializer = GenreSerializer(genre, many=True)

    return Response(serializer.data)


######################################################################
@api_view(['GET', 'POST'])
def comment(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)

    if request.method == "GET":
        comments = review.comment_set.all()
        serializer = CommentReadSerializer(comments, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        print(request.data)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print("2")
            serializer.save(review=review, user=request.user)
            print("3")
            return Response(serializer.data, status=201)


######################################################################
@api_view(['PUT', 'DELETE'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if comment.user != request.user:
        return Response({"message":"User isn't authenticated"}, status=401)

    if request.method == "PUT":
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    
    if request.method == "DELETE":
        comment.delete()
        return Response({"message":"clear delete"}, status=204)


######################################################################
def api_list(request):
    return render(request, 'movies/apilist.html')
    
######################################################################
# youtube, stil api(세울)
@api_view(['GET'])
def youtube(request, movie_pk):
    youtube = youtube_key.objects.filter(movie_id=movie_pk)
    still = stillcut.objects.filter(movie_id=movie_pk)
    if youtube.exists() or still.exists():
        youtubeNstill ={}
        if youtube.exists():
            serializer = Youtube_keySerializer(youtube, many=True)
            youtubeNstill['youtube'] = serializer.data
        if still.exists():
            serializer = Still_cutSerializer(still, many=True)
            youtubeNstill['still'] = serializer.data
        return Response(youtubeNstill, status=200)
    else:
        return Response(status=404)
