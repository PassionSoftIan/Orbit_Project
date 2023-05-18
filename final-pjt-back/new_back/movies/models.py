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
class stillcut(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    img_url = models.TextField()

########################################################
class youtube_key(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    key = models.CharField(max_length=20)

    

