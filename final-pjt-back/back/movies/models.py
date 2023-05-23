from django.db import models
from django.conf import settings


########################################################
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

########################################################
class Movie(models.Model):
    title = models.CharField(max_length=50)
    overview = models.TextField()
    poster_path = models.TextField()
    release_date = models.CharField(max_length=50)
    vote_average = models.FloatField()
    tagline = models.TextField(blank=True)
    revenue = models.FloatField()
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return f"{self.title}"
    

########################################################
class Review(models.Model):
    vote = models.FloatField()
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updateed_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="myreviews")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # 리뷰 작성자 이름 게시하기 위해서 field작성 (인식)


########################################################
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)


########################################################
class stillcut(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    img_url = models.TextField()

########################################################
class youtube_key(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    key = models.CharField(max_length=20)


    

