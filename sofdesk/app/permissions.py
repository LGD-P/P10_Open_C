from rest_framework import permissions


class ProjectPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True


class ContributorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True


class IssuePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True


class CommentPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
