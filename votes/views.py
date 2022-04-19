from django.shortcuts import render
from django.http import HttpResponse
from .models import Player, PlayerVotes

# Create your views here.
def index(request):
    return HttpResponse("<h1>pekoepa</h1> mis panas")

def vote(request):
    numero = Player.objects.all().count()
    context = {
        'numero': numero,
    }
    return render(request,'index.html', context=context)
