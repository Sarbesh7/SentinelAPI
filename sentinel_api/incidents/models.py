from django.db import models
from accounts.models import User



class Incident(models.Model):
    category_choices=(
        ('accident', 'Accident'),
        ('harrasatment', 'Harrasatment'),
        ('fire', 'Fire'),
        ('cyberabuse', 'Cyber Abuse'),
        ('emergency', 'Emergency'),
        ('other', 'Other')  
    )
    priority_choices=(
        ('low', 'Low'), 
        ('medium', 'Medium'), 
        ('high', 'High')
    )
    status_choices=(
        ('reported', 'Reported'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed')
    )
    title=models.CharField(max_length=255)
    description=models.TextField()
    location=models.CharField(max_length=255)
    images=models.ImageField(upload_to='incident_images/', blank=True, null=True)
    videos=models.FileField(upload_to='incident_videos/', blank=True, null=True)
    
    category=models.CharField(max_length=50, choices=category_choices)
    priority=models.CharField(max_length=20, choices=priority_choices, default='medium')
    status=models.CharField(max_length=20, choices=status_choices, default='reported')
    
    reported_by=models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_incidents') #reported user
    assigned_to=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_incidents') #assigned responder
    reported_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title