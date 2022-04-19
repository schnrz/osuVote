from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Player(AbstractUser):
    nick = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=20
    )
    user_id = models.IntegerField(default=None, null=True)
    user_avatar = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=100
    )
    cover_url = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=200
    )

class PlayerVotes(models.Model):
    voter_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="fk_voter_id")
    osu_id = models.IntegerField()
    nick = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=20
    )
    avatar_url = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=200
    )
    points = models.IntegerField()