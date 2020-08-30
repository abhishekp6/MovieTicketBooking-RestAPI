from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'

class TicketUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ('name','contact_number',)

class TicketTimeUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ('start_time',)

class TicketViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ('name','contact_number','status',)