"""osuVote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from votes import views

urlpatterns = [
    path('', views.index, name='index')
]

from django.contrib import admin

urlpatterns += [
    path('admin/', admin.site.urls),
]

# Use include() to add paths from the catalog application
from django.urls import include

urlpatterns += [
    path('votes/', include('votes.urls')),
]
    
# Add URL maps to redirect the base URL to our application
# this thing sends ./ to ./votes/
# from django.views.generic import RedirectView
# urlpatterns += [
#     path('', RedirectView.as_view(url='votes/', permanent=True))
# ]

# Use static() to add URL mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Alternate way to add all the above stuff
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('catalog/', include('catalog.urls')),
#     path('', RedirectView.as_view(url='catalog/')),
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)