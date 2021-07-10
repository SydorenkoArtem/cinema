from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """User profile model implementation"""

    class Meta:
        db_table = "auth_userprofile"
        verbose_name = "user profile"
        verbose_name_plural = "user profiles"

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="user",
        related_name="profile",
    )

    avatar = models.ImageField(
        upload_to="static/images/user",
        default="static/images/default/user.png",
    )

    balance = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=1_000.00,
        verbose_name="balance amount",
        help_text="A positive numeric value. Defaults to $1,000.00",
    )

    def __repr__(self):
        """Return a string representation of an instance"""

        return f"<UserProfile ('{self}')>"

    def __str__(self):
        """Return a string version of an instance"""

        return self.user.__str__()
