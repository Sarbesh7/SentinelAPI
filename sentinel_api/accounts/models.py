from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
    
    role =(
        ('Admin', 'Admin'),
        ('Citizen', 'Citizen'),
        ('Responder', 'Responder')
    )
    role = models.CharField(max_length=20, choices=role, default='Citizen')
   
    def __str__(self):
        return self.username
