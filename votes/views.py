from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Player, PlayerVote
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

import requests

from votes import osu_auth

# Create your views here.
def index(request):
    return render(request, 'home.html')

# TODO this isn't working properly, should uhhh idk, change login_url
@login_required(login_url='auth')
def get_auth_player(request: HttpRequest):
    return JsonResponse({'msg': 'Authenticated'})

def auth_redir(request: HttpRequest) -> JsonResponse:
    return redirect(osu_auth.auth_url())

def vote(request: HttpRequest):
    # numero = Player.objects.all().count()
    code = request.GET.get('code')
    grant = osu_auth.get_osu_user(code)

    player = authenticate(request, player=grant)
    osu_user = list(player).pop()
    print(player)
    login(request, osu_user)

    context = {
        'codigo': grant.json().get('avatar_url'),
    }    
    return render(request,'index.html', context=context)
