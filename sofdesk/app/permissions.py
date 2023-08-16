from rest_framework import permissions


from app.models import Contributor, Issue, Comment, Project


class IsContributorPermission(permissions.BasePermission):
    def has_permission(self, request, view):

        project = request.data.get('project')
        contributor = request.data.get('contributor')
        issue = request.data.get('issue')
        comment = request.data.get('comment')

        if request.method in permissions.SAFE_METHODS:
            return True
        elif view.action == "create" and project:
            return True
        elif view.action == "create" and contributor:
            return True
        elif view.action == "create" and issue:
            return True
        elif view.action == "create" and comment:
            return True

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
