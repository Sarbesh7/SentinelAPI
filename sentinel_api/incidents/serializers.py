from . import models    
from rest_framework import serializers  



class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Incident
        fields = '__all__'
        
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None
        return models.Incident.objects.create(reported_by=user, **validated_data)
    