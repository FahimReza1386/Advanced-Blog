from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models.user import User
from accounts.services.profile_service import ProfileService


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ProfileService.create_for_user(instance)