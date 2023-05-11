"""kahootclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from restServer import views
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
]

# Services URLs
urlpatterns += [
    path('', RedirectView.as_view(url='services/', permanent=True)),
    path('services/', include('services.urls')),
]

# Authentication URLs
urlpatterns += [
    path('accounts/', include('models.urls')),
]

# Rest Server router & URLs
router = routers.DefaultRouter()
router.register('participant', views.ParticipantViewSet)
router.register('games', views.GameViewSet)
router.register('guess', views.GuessViewSet)
urlpatterns += [
    path('api/', include(router.urls)),
]
