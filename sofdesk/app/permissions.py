from rest_framework import permissions


from app.models import Contributor, Issue, Comment, Project


class IsContributorPermission(permissions.BasePermission):
    def has_permission(self, request, view):

        project = request.data.get('project')

        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow any user to creat a new project
        elif view.action == "create" and not project:
            return True
        # Only contributor can create contributor, issue and comment
        elif view.action == "create":
            return Contributor.objects.filter(user=request.user, project=project).exists()
        return True

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            if isinstance(obj, Comment):
                project = obj.issue.project
            elif isinstance(obj, (Issue, Contributor)):
                project = obj.project
            elif isinstance(obj, Project):
                project = obj
            else:
                return True

            return Contributor.objects.filter(
                user=request.user, project=project).exists()

        return True


class IsAuthorPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if view.action in ['update', 'partial_update', 'destroy']:
            return obj.author == request.user
        return True
