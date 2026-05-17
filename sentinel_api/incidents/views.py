from django.shortcuts import render
from rest_framework.views import APIView
from . import serializers
from . import models
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission
from accounts.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'admin'
class IsResponder(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'responder'



class IncidentView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAdmin()]
        return [IsAuthenticated()]
    
    def get(self, request):
        incidents = models.Incident.objects.all()
        
        # Filter by category
        category = request.query_params.get('category')
        if category:
            incidents = incidents.filter(category=category)
        
        # Search by title
        search = request.query_params.get('search')
        if search:
            incidents = incidents.filter(title__icontains=search)
        
        # Ordering
        ordering = request.query_params.get('ordering')
        if ordering:
            incidents = incidents.order_by(ordering)
        
        serializer = serializers.IncidentSerializer(incidents, many=True)
        return Response(serializer.data)
    
    
    
    
    
    def post(self, request):    
        data=request.data
        serializer=serializers.IncidentSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save(reported_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class IncidentDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method == 'PUT':
            return [IsResponder()]
        elif self.request.method == 'DELETE':
            return [IsAdmin()]
        return [IsAuthenticated()]
    
    
    def get_object(self, id):
        try:
            return models.Incident.objects.get(id=id)
        except models.Incident.DoesNotExist:
            return None
    
    def get(self, request, id):
        incident = self.get_object(id)
        if not incident:
            return Response({'error': "Incident not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = serializers.IncidentSerializer(incident)
        return Response(serializer.data)
    
    def put(self,request,id):
       
        incident=self.get_object(id)
        if not incident:
            return Response({'error':"Incident not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer=serializers.IncidentSerializer(incident, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   
    def delete(self, request, id):
        incident=self.get_object(id)
        
        if not incident:
            return Response({'error':"Incident not found"}, status=status.HTTP_404_NOT_FOUND)
        
        incident.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
