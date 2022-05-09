from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Player, PlayerVotes
from django.shortcuts import redirect
import requests

from votes import osu_auth

# Create your views here.
def index(request):
    return render(request, 'home.html')
    # return redirect(osu_auth.auth_url())

def auth_redir(request: HttpRequest) -> JsonResponse:
    return redirect(osu_auth.auth_url())

def vote(request):
    # numero = Player.objects.all().count()
    code = request.GET.get('code')
    context = {
        #'codigo': osu_auth.auth_grant(code),
    }
    return render(request,'index.html', context=context)
