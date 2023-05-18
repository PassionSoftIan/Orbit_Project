from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nick_name = models.CharField(blank=True, max_length=10)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
