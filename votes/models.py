# from django.forms import BooleanField
# from djongo import models
# from django.contrib.postgres.fields import ArrayField
# from django import forms
#from django.db import models

# Create your models here.



# class Votos_std(models.Model):
    # puntos = models.IntegerField()
    # id_player = models.IntegerField()
    # nickname = models.CharField(max_length=20)
#     class Meta:
#         abstract = True

# class Votos_taiko(models.Model):
#     puntos = models.IntegerField()
#     id_player = models.IntegerField()
#     nickname = models.CharField(max_length=20)
#     class Meta:
#         abstract = True

# class Votos_ctb(models.Model):
#     puntos = models.IntegerField()
#     id_player = models.IntegerField()
#     nickname = models.CharField(max_length=20)
#     class Meta:
#         abstract = True

# class Votos_mania(models.Model):
#     puntos = models.IntegerField()
#     id_player = models.IntegerField()
#     nickname = models.CharField(max_length=20)
#     class Meta:
#         abstract = True

# class Votos_std_form(forms.ModelForm):
#     class Meta:
#         model = Votos_std
#         fields = (
#             'puntos', 'id_player', 'nickname'
#         )

# class Votos_taiko_form(forms.ModelForm):
#     class Meta:
#         model = Votos_taiko
#         fields = (
#             'puntos', 'id_player', 'nickname'
#         )

# class Votos_ctb_form(forms.ModelForm):
#     class Meta:
#         model = Votos_ctb
#         fields = (
#             'puntos', 'id_player', 'nickname'
#         )

# class Votos_mania_form(forms.ModelForm):
#     class Meta:
#         model = Votos_mania
#         fields = (
#             'puntos', 'id_player', 'nickname'
#         )
# class Usuario(models.Model):
    # nickname = models.CharField(max_length=20)#preguntar el lengh
    # id_osu_usuario = models.IntegerField()
    # puede_votar = BooleanField()

#     class Meta:
#         votos_std = models.ArrayField(
#             model_container=Votos_std,
#             model_form=Votos_std_form
#         )
#         votos_taiko = models.ArrayField(
#             model_container=Votos_taiko,
#             model_form=Votos_taiko_form
#         )
#         votos_ctb = models.ArrayField(
#             model_container=Votos_ctb,
#             model_form=Votos_ctb_form
#         )
#         votos_mania = models.ArrayField(
#             model_container=Votos_mania,
#             model_form=Votos_mania_form
#         )
                        


from djongo import models
from django import forms

class Player(models.Model):
    player_id = models.IntegerField()
    username = models.CharField(max_length=15)
    points = models.SmallIntegerField()

    class Meta:
        abstract = True

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = (
            'player_id', 'username', 'points'
        )

class Vote(models.Model):
    player_id = models.IntegerField()
    username = models.CharField(max_length=15)
    avatar_url = models.CharField(max_length=100)
    cover_url = models.CharField(max_length=100)

    players = models.ArrayField(
        model_container=Player,
        model_form_class=PlayerForm
    )

    objects = models.DjongoManager()