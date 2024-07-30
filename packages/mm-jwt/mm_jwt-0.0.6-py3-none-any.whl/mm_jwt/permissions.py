from rest_framework import permissions
from .models import CustomToken


class JTIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        is_authenticated = CustomToken.verify(request=request)
        return is_authenticated
