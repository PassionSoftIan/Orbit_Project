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
    popularity = models.FloatField()
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return f"{self.title}"
    

########################################################
class Review(models.Model):
    vote = models.FloatField()
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updateed_at = models.DateTimeField(auto_now=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


########################################################
class Comment(models.Model):
    content = models.TextField()
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)


########################################################


    

