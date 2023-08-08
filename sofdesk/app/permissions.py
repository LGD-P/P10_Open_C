from rest_framework import permissions
from django.db.models import Q

from app.models import Contributor, Project, Issue, Comment


class ProjectPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        if request.method == 'GET' and Contributor.objects.filter(
                Q(author=request.user) | Q(project__author=request.user)):
            return True


class ContributorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True


class IssuePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        """
        if Contributor.objects.filter(
                Q(author=request.user) | Q(project__author=request.user)):
            return True
        """


class CommentPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        """
        if Issue.objects.filter(
                Q(author=request.user) | Q(project__author=request.user)):
            return True
        """


"""

"""
