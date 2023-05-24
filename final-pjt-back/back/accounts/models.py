from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Review

# Create your models here.
class User(AbstractUser):
    nick_name = models.CharField(blank=True, max_length=10)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    like_reviews = models.ManyToManyField(Review, related_name='liked_user')
    coins = models.IntegerField(default = 0)