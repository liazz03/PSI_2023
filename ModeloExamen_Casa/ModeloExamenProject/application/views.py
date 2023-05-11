from django.shortcuts import render
from typing import Any, Dict
from django.db.models.query import QuerySet

from django.views import generic
from .models import Channel, Suscription
from django.core.exceptions import ObjectDoesNotExist

class ChannelView(generic.ListView):

    model = Channel
    template_name = "channel.html"
    context_object_name = "subscriptions"

    def get_queryset(self):

        try:
            channell = Channel.objects.get(id=self.kwargs['pk'])
            subscriptions = Suscription.objects.filter(channel=channell)
            return subscriptions
        
        except ObjectDoesNotExist:
            return []

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        try:
            Channel.objects.get(id=self.kwargs['pk'])

        except ObjectDoesNotExist:
            context['error'] = "Channel of pk: " + str(self.kwargs['pk']) + " is not in database"
            return context

        return context


