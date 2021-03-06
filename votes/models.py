from django.db import models
from django.contrib.auth.models import AbstractUser 
from .managers import PlayerOAuth2Manager

class Player(models.Model):
    objects = PlayerOAuth2Manager()

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
    last_login = models.DateTimeField(null=True)
    def __str__(self):
        # String to give nick attr to admin site
        return self.nick

    # this may be useful later 
    # def get_absolute_url(self):
    #     return reverse('model-detail-view', args=[str(self.user_id)])

# TODO: check if this works ffs
# def is_authenticated(self, request):
#     return True

class PlayerVote(models.Model):
    voter = models.ForeignKey(Player, on_delete=models.CASCADE)
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

    def __str__(self):
        # String to give nick attr to admin site
        return self.nick