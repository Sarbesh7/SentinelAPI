from . import models    
from rest_framework import serializers  



class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Incident
        fields = '__all__'
        read_only_fields = ['reported_by', 'reported_at']
        
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None
        return models.Incident.objects.create(reported_by=user, **validated_data)
    
    def validate_images(self, value):
        if value:
            valid_types = ['image/jpeg', 'image/png', 'image/gif']
            if value.content_type not in valid_types:
                raise serializers.ValidationError("Invalid image format")
            if value.size > 5 * 1024 * 1024:   # 5MB limit
                raise serializers.ValidationError("Image too large")
        return value
    