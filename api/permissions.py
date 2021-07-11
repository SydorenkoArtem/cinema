from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class UserAPIPermission(BasePermission):

    def has_permission(self, request, obj):
        return obj == request.user or request.user.is_staff
