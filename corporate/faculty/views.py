from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.decorators import permission_required
from .serializers import FacultySerializer
from .models import Faculty

# Create your views here.

class FacultyView(APIView):
       
    
    permission_classes = [permissions.IsAdminUser]
    
    
    def get(self, request, format=None):
        
        queryset = Faculty.objects.all()
        serializer_class = FacultySerializer(queryset,many=True)
         
        return Response(serializer_class.data, status=200)