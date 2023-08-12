from rest_framework import permissions
from django.db.models import Q

from app.models import Contributor


class UnlimitedAcces(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False


class ProjectPermission(permissions.BasePermission):
    # paramétrer les has permisssion en fonction des views action

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
        """
         if request.user == obj.author or request.user == obj.project.author:
             return True
         if view.action == "create" and not Contributor.objects.filter(
                 Q(author=request.user) | Q(project__author=request.user)):
             return False"""


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
