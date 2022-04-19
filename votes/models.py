from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone

class Usuario(AbstractUser):
    nickname =  models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=15
    )
    osu_id = models.IntegerField()
    avatar_url = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=30
    )
    cover_url = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=30
    )

class Votos(models.Model):
    id_votante = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="fk_id_votante")
    puntos = models.IntegerField()
    id_osu = models.IntegerField()
    nickname = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=15
    )
    url_avatar = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=15
    )