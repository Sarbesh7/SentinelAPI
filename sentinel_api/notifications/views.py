from django.shortcuts import render
from accounts.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from . import serializers, models


class NotificationView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # Get only the current user's notifications
        notifications = request.user.notifications.all().order_by('-created_at')
        serializer = serializers.NotificationSerializer(notifications, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # Create a new notification for the current user
        serializer = serializers.NotificationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotificationDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self, user, notification_id):
        try:
            return models.Notification.objects.get(id=notification_id, user=user)
        except models.Notification.DoesNotExist:
            return None
    
    def patch(self, request, id):
        # Mark notification as read
        notification = self.get_object(request.user, id)
        if not notification:
            return Response({'error': 'Notification not found'}, status=status.HTTP_404_NOT_FOUND)
        
        notification.is_read = request.data.get('is_read', notification.is_read)
        notification.save()
        serializer = serializers.NotificationSerializer(notification)
        return Response(serializer.data)
    
    def delete(self, request, id):
        # Delete notification
        notification = self.get_object(request.user, id)
        if not notification:
            return Response({'error': 'Notification not found'}, status=status.HTTP_404_NOT_FOUND)
        
        notification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)