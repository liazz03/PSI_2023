from django.shortcuts import render
from .serializers import ChannelSerializer, UserSerializer, SuscriptionSerializer
from application.models import Channel, User, Suscription
from rest_framework import viewsets

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SuscriptionViewSet(viewsets.ModelViewSet):
    queryset = Suscription.objects.all()
    serializer_class = SuscriptionSerializer

#TODO PUT DELETE??