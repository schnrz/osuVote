from django.urls import path

from . import views

urlpatterns = [path('', views.vote, name='vote'),
               path('vote/auth', views.auth_redir, name='auth')
]