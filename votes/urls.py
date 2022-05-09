from django.urls import path

from . import views

urlpatterns = [path('', views.vote, name='vote'),
               path('vote/auth', views.auth_redir, name='auth'),
               path('vote/voting', views.voting, name='voting'),
               path('vote/stats', views.auth_redir, name='auth')
]