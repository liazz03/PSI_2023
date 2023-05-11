from django.shortcuts import render

#added imports
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Channel, Suscription
# Create your views here.

class ChannelView(generic.DetailView):
    model = Channel
    template_name = 'channel.html' 
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        channelobj = self.get_object()

        context['subscriptions'] = Suscription.objects.filter(channel = channelobj)
        context['channelName'] = channelobj.channelName
        #TODO: return error through error variable
        return context

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Channel, id=pk_)
