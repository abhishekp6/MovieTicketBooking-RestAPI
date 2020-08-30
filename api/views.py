from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ticket
from .serializers import TicketSerializer
from .serializers import TicketTimeUpdateSerializer


class ticketlist(APIView):
    def get(self,request):
        ticket1 = Ticket.objects.all()
        serializer = TicketSerializer(ticket1,many=True)
        return Response(serializer.data)

class bookTicket(APIView):
    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class updateTicketTime(APIView):
    def post(self, request, pk):
        ticket2 =  Ticket.objects.get(ticket_id=pk)
        serializer = TicketTimeUpdateSerializer(instance=ticket2, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)