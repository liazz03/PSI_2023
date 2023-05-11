import os
from django.core.management.base import BaseCommand
from application.models import Channel
from application.models import User
from application.models import Suscription
from django.contrib.auth import get_user_model

import random
from datetime import date


# The name of this class is not optional must be Command
# otherwise manage.py will not process it properly
class Command(BaseCommand):
    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = """populate exam database
           """
    # if you want to pass an argument to the function
    # uncomment this line
    # def add_arguments(self, parser):
    #    parser.add_argument('publicId',
    #        type=int,
    #        help='game the participants will join to')
    #    parser.add_argument('sleep',
    #        type=float,
    #        default=2.,
    #        help='wait this seconds until inserting next participant')

    def __init__(self, sneaky=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # "if 'RENDER'" allows you to deal with different
        # behaviour in render.com and locally
        # That is, we check a variable ('RENDER')
        # that is only defined in render.com
        if 'RENDER' in os.environ:
            pass
        else:
            pass

    # handle is another compulsory name, do not change it"
    # handle function will be executed by 'manage populate'
    def handle(self, *args, **kwargs):
        "this function will be executed by default"

        self.cleanDataBase()   # clean database

        self.user()  # create users
        self.channel()  # create questionaries
        self.suscription()  # create questions

    def cleanDataBase(self):

        # borra superususario
        User_model = get_user_model()
        User_model.objects.all().delete()

        # borra objetos
        User.objects.all().delete()
        Channel.objects.all().delete()
        Suscription.objects.all().delete()

        print("clean Database")

    def user(self):
        " Insert users"
        print("Creating Users...")

        #crea superusurio
        User_model = get_user_model()
        User_model.objects.create_superuser('alumnodb', 'admin@myproject.com', 'alumnodb')

        name = "antonio2985"
        user = User(id = 1001, userName = name)
        user.save()

        name = "respetaCamiones124"
        user = User(id = 1002, userName = name)
        user.save()

        name = "asierUR"
        user = User(id = 1003, userName = name)
        user.save()


    def channel(self):
        "insert channels"
        print("Creating channels...")

        name = "elxokasTV"
        channel = Channel(id = 1001, channelName = name)
        channel.save()

        name = "ibai"
        channel = Channel(id = 1002, channelName = name)
        channel.save()

        name = "playz"
        channel = Channel(id = 1003, channelName = name)
        channel.save()


    def suscription(self):
        " insert questions, assign randomly to questionnaires"
        print("Inserting suscriptions...")

        suscripcion = Suscription(id = 1001, channel = Channel.objects.get(channelName = "elxokasTV"), 
                                  user = User.objects.get(userName = "antonio2985"),
                                  suscriptionDate = date(2023,4,5))
        
        suscripcion.save()
        
        suscripcion = Suscription(id = 1002, channel = Channel.objects.get(channelName = "ibai"), 
                            user = User.objects.get(userName = "respetaCamiones124"),
                            suscriptionDate = date(2023,4,11))
        
        suscripcion.save()

        suscripcion = Suscription(id = 1003, channel = Channel.objects.get(channelName = "playz"), 
                            user = User.objects.get(userName = "asierUR"),
                            suscriptionDate = date(2023,4,12))
        
        suscripcion.save()
