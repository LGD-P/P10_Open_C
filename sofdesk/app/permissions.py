from rest_framework import permissions
from django.db.models import Q
from app.models import Contributor, Issue, Comment, Project


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
        if view.action == 'create':

            project_id = request.data.get('project')
            project = Project.objects.get(id=project_id)
            return Project.objects.filter(author=request.user, project_id=project).exists()
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'partial_update', 'destroy'] or view.action not in permissions.SAFE_METHODS:
            return obj.author == request.user
        return True


class IssuePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            # Make sure the user is a contributor to the project
            project_id = request.data.get('project')
            project = Project.objects.get(id=project_id)
            return Contributor.objects.filter(author=request.user, project=project).exists()

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Autorise unsafe method if this object author
        # is the authenticated user
        if view.action in ['update', 'partial_update', 'destroy']:
            return obj.author == request.user

        # Autorise SAFE_METHODS if user is author or has issue assigned
        if request.method in permissions.SAFE_METHODS:
            return Issue.objects.filter((Q(author=request.user) | Q(assign_to=request.user)))


class CommentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            # Make sure the user is the author of the issue or the issue is assigned to the user
            issue_id = request.data.get('issue')
            issue = Issue.objects.get(id=issue_id)
            return issue.author == request.user or issue.assign_to == request.user
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Autorise unsafe method if this object author
        # is the authenticated user
        if view.action in ['update', 'partial_update', 'destroy']:
            return obj.author == request.user

        if request.method in permissions.SAFE_METHODS:
            if Comment.objects.filter(Q(author=request.user) | Q(issue__assign_to=request.user) | Q(issue__author=request.user)):
                return True
