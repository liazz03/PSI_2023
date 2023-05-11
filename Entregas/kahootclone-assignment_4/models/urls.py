from django.urls import include, path
from . import views as models_views

# Authentication urls (login, logout, pwd management)
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]


urlpatterns += [
    path('signup', models_views.SignUpView.as_view(), name='signup'),
]
