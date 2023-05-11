from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

#added imports
from django.views import generic
from .models import Channel, Suscription
# Create your views here.

class ChannelView(generic.ListView):

    model = Channel
    template_name = 'channel.html' 
    context_object_name = 'subscriptions'

    def get_queryset(self):
        subscriptions = []

        channell = Channel.objects.filter(id=self.kwargs['pk']).first()

        if channell is not None :
            subscriptions = Suscription.objects.filter(channel=channell)
        
        return subscriptions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        channel = Channel.objects.filter(id = self.kwargs['pk']).first()

        if channel is None:
            context['error'] = f"No channels found with pk: {self.kwargs['pk']}" 
            return context 
        
        return context

