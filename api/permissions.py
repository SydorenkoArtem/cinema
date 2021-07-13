from rest_framework.permissions import BasePermission


class UserStaffPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class UserAPIPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user


class UserOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id


class ProfileOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user.id
