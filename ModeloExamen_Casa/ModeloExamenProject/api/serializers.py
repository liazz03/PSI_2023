from application.models import Channel, User, Suscription
from rest_framework import serializers



class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class SuscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Suscription
        fields = '__all__'
