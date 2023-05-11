from django.urls import path
from . import views

urlpatterns = [
    path('channel/<int:pk>', views.ChannelView.as_view(), name='channel-view'),
]