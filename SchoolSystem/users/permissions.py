# users/permissions.py

from rest_framework.permissions import BasePermission
from .models import UserTypeChoices


class CanViewUsers(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
