#signals will create profiles for users when they are create automatically based on their role



from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, CitizenProfile, ResponderProfile  


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'citizen':
            CitizenProfile.objects.create(user=instance)
        elif instance.role == 'responder':
            ResponderProfile.objects.create(user=instance)
