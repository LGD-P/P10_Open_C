from rest_framework import permissions
from django.db.models import Q
from app.models import Project, Contributor, Issue


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
            return Contributor.objects.filter(project=obj, author=request.user).exists()


class IsAuthorPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'partial_update', 'destroy'] or view.action not in permissions.SAFE_METHODS:
            return obj.author == request.user
        return True


class IssuePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Autorise unsafe method if this object author
        # is the authenticated user
        if view.action in ['update', 'partial_update', 'destroy']:
            return obj.author == request.user

        # Autorise SAFE_METHODS if user is author or has issue assigned
        if request.method in permissions.SAFE_METHODS:
            return Issue.objects.filter((Q(author=request.user) | Q(assign_to=request.user)))
