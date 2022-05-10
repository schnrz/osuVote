from django.urls import path

from . import views

urlpatterns = [path('', views.vote, name='vote'),
               path('auth', views.auth_redir, name='auth'),
               path('authuser', views.get_auth_player, name='authuser')
]