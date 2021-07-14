from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from user.models import UserProfile


@receiver(post_save, sender=User)
def handle_user_post_save_signal(instance, created, **kwargs):
    """Handle a user model post_save signal"""

    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(instance=None, created=False, **kwargs):
    """Handle a user token post_save signal"""

    if created:
        Token.objects.create(user=instance)
