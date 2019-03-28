from rest_framework import permissions
from rest_framework.authtoken.models import Token


class IsSuperUser(permissions.BasePermission):
    """
    Permission class to allow only superusers
    """

    def has_permission(self, request, view):
        token_key = request.META.get('HTTP_AUTHORIZATION', '')
        try:
            token = Token.objects.get(key=token_key[6:])
        except Exception as error:
            return False
        return token.user.is_superuser
