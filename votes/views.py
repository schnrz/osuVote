from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>pekoepa</h1> mis panas")

def vote(request):
    return HttpResponse("<h1>prueba</h1>")
