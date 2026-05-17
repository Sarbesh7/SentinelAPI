from .import models
from rest_framework import serializers

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = '__all__'
        read_only_fields = ['user', 'created_at']
        
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None
        return models.Notification.objects.create(user=user, **validated_data)