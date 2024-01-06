from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField('email address', blank=False, unique=True)
    first_name = models.CharField('first name', blank=False, max_length=120)
    last_name = models.CharField('last name', blank=False, max_length=120)
    followers = models.IntegerField('followers', blank=True, default=0)
    following = models.IntegerField('following', blank=True, default=0)
    profileIMG = models.CharField(max_length=300, blank=True, default='')


class Follow(models.Model):
    follower_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    followee_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='followee')
