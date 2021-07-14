from rest_framework.permissions import BasePermission


class UserStaffPermission(BasePermission):
    """Permission for staff implementation"""

    def has_permission(self, request, view):
        return request.user.is_staff


class UserAPIPermission(BasePermission):
    """Permission for user implementation"""

    def has_permission(self, request, view):
        return request.user


class UserOwnerPermission(BasePermission):
    """Permission for owner implementation"""

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id


class ProfileOwnerPermission(BasePermission):
    """Permission for owner of object implementation"""

    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user.id
