from django.urls import path

from . import views

urlpatterns = [path('', views.vote, name='vote'),
               # path('vote/',views.vote, name='vote')
]