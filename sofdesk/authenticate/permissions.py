from rest_framework import permissions


class UserModifyPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user.user_id
