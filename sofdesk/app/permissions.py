from rest_framework import permissions


class IsContributorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Autorise unsafe method if this object author
        # is the authenticated user
        if view.action in ['update', 'partial_update', 'destroy']:
            return obj.author == request.user

        # Autorise SAFE_METHODS if user is contributor to project
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
