from rest_framework import permissions


class UserModifyPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.user_id == request.user:
            return True
