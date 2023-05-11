from django.db import models
from django.urls import reverse
import uuid
from datetime import date

# Create your models here.
class Channel(models.Model):
    channelName = models.CharField(max_length=200,
                            help_text='Enter a channel name')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.channelName

class User(models.Model):
    userName = models.CharField(max_length=200,
                            help_text='Enter a user name')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.userName
    
class Suscription(models.Model):

    channel = models.ForeignKey('Channel', on_delete=models.SET_NULL, null=True)

    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    suscriptionDate = models.DateField(null=True, blank=False)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.user.userName} : {self.channel.channelName})'
