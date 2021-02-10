from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from . models import Members
from .serializers import MemberSerializer
    
class members(viewsets.ViewSet):
    """To Get The Memebers Details"""
    def list(self,request):
        query = Members.objects.all()
        # To get All Objects From the models and store in query object

        serial = MemberSerializer(query,many=True)
        #To serialize the objects data and return to the request server
        
        return Response({'Member': serial.data})