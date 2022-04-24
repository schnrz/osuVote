from django.urls import path

from . import views

urlpatterns = [path('home/', views.index, name='index'),
               # path('vote/',views.vote, name='vote')
]