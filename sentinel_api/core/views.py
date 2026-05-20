from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.permissions import BasePermission

from incidents.models import Incident, models
from accounts.models import User
from incidents.serializers import IncidentSerializer
from accounts.serializers import UserSerializer
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class IsResponder(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'responder'


class IsCitizen(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'citizen'


class CitizenDashboard(APIView):
    permission_classes = [IsCitizen]

    def get(self, request):
        user = request.user
        incidents = Incident.objects.filter(reported_by=user).order_by('-reported_at')
        serializer = IncidentSerializer(incidents, many=True)
        pending_incidents = incidents.filter(status='reported').count()
        resolved_incidents = incidents.filter(status='resolved').count()
        return Response({
            'pending_incidents': pending_incidents,
            'resolved_incidents': resolved_incidents,
            'incidents': serializer.data
        })

class ResponderDashboard(APIView):
    permission_classes = [IsResponder]

    def get(self, request):
        user = request.user
        assigned_incidents = Incident.objects.filter(assigned_to=user).order_by('-reported_at')
        serializer = IncidentSerializer(assigned_incidents, many=True)
        pending_incidents = assigned_incidents.filter(status='reported').count()
        in_progress_incidents = assigned_incidents.filter(status='in_progress').count()
        resolved_incidents = assigned_incidents.filter(status='resolved').count()
        return Response({
            'pending_incidents': pending_incidents,
            'in_progress_incidents': in_progress_incidents,
            'resolved_incidents': resolved_incidents,
            'assigned_incidents': serializer.data
        })

class AdminDashboard(APIView):   
    permission_classes = [IsAdminUser]

    def get(self, request):
        incidents = Incident.objects.all().order_by('-reported_at')
        serializer = IncidentSerializer(incidents, many=True)
        return Response(serializer.data)


class AdminUserManagement(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, user_id=None):
        if user_id:
            # Get a specific user
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            # Get all users
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

    def put(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        new_role = request.data.get('role')
        old_role = user.role
        
        if not new_role:
            return Response({'error': 'Role field is required'}, status=status.HTTP_400_BAD_REQUEST)

        valid_roles = ['admin', 'citizen', 'responder']
        if new_role not in valid_roles:
            return Response({'error': f'Invalid role. Must be one of: {", ".join(valid_roles)}'}, status=status.HTTP_400_BAD_REQUEST)

        # Clean up old profile if role is changing
        if old_role != new_role:
            if old_role == 'citizen' and hasattr(user, 'citizen_profile'):
                user.citizen_profile.delete()
            elif old_role == 'responder' and hasattr(user, 'responder_profile'):
                user.responder_profile.delete()

        user.role = new_role
        
        # Sync is_staff flag with admin role
        user.is_staff = (new_role == 'admin')
        user.save()
        
        serializer = UserSerializer(user)
        return Response({
            'message': f'User role updated to {new_role}',
            'user': serializer.data
        }, status=status.HTTP_200_OK)