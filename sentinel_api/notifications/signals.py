from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
from incidents.models import Incident


@receiver(post_save, sender=Incident)
def create_incident_notification(sender, instance, created, **kwargs):
    
    if created:
        message = f"Your incident '{instance.title}' has been reported successfully."
        Notification.objects.create(
            user=instance.reported_by,
            message=message,
            is_read=False
        )
