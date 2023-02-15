from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserNet, Profile, PrivacySettings


@receiver(post_save, sender=UserNet)
def create_user(sender, instance, created,**kwargs):
    if created:
        PrivacySettings.objects.create(
            profile=Profile.objects.create(user=instance)
        )