from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('citizen', 'Citizen'),
        ('responder', 'Responder')
    )
    
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='citizen')
   
    def __str__(self):
        return self.username

class CitizenProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='citizen_profile')
    address = models.CharField(max_length=255, blank=True, null=True)
    emergency_contact = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    

class ResponderProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='responder_profile')
    department = models.CharField(max_length=255, blank=True, null=True)
    badge_number = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"    