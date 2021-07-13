import datetime

from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed

from cinema import settings


class ExpiringTokenAuthentication(TokenAuthentication):
    """
    If token is expired then it will be removed
    and new one with different key will be created
    """

    def handle_token(self, token):
        if self.is_expired(token):
            token.delete()
            raise AuthenticationFailed("The Token is expired")
        token.created = timezone.now()
        return token

    @staticmethod
    def is_expired(token):
        time_elapsed = timezone.now() - token.created
        expire = datetime.timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS)

        return time_elapsed > expire

    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
            self.handle_token(token)
        except Token.DoesNotExist:
            raise AuthenticationFailed("Invalid Token")

        return token.user, token
