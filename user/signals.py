"""
User Application Signals
========================

"""

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import UserProfile


@receiver(post_save, sender=User)
def handle_user_post_save_signal(sender, instance, created, *args, **kwargs):
    """Handle a user model post_save signal"""

    if created:
        UserProfile.objects.create(user=instance)
