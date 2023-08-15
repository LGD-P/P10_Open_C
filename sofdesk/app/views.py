from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


from django.db.models import Q
from app.models import (Project, Contributor,
                        Issue, Comment)
from app.serializers import (ProjectSerializer, ContributorSerializer,
                             IssueSerializer, CommentSerialiser)
from app.permissions import (
    IsContributorPermission, IsAuthorPermissions, IssuePermission, CommentPermission)


class ProjectViewset(ModelViewSet):

    """Manage CRUD operations on Project object

    Args:
        ModelViewSet (_type_): base viewset class to manage C.R.U.D
    """

    serializer_class = ProjectSerializer
    permission_classes = [IsContributorPermission, IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """Filter queryset to only show projects that logged user is contributor for"""
        # projects = Project.objects.filter(contributor__author=self.request.user).prefetch_related('contributor_set')
        # projects = Project.objects.all()
        projects = projects = Project.objects.filter(
            contributor__author=self.request.user).prefetch_related('contributor_set')
        return projects


class ContributorViewset(ModelViewSet):
    """Manage CRUD operations on Contributor object

    Args:
        ModelViewSet (_type_): base viewset class to manage C.R.U.D
    """

    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, IsAuthorPermissions]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """Filter queryset to only show contributor as logged user """

        # contributors = Contributor.objects.all()
        # contributors = Contributor.objects.select_related('author').filter(Q(author=self.request.user))
        contributors = Contributor.objects.select_related(
            'author').filter(Q(author=self.request.user))

        return contributors


class IssuetViewset(ModelViewSet):
    """_Manage CRUD operations on Issue object

    Args:
        ModelViewSet (_type_): base viewset class to manage C.R.U.D
    """

    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IssuePermission]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """Simple query_set to get all Issue that logged user is author or was assignedto

        Returns:
            _type_:all Issue
        """
        # issues = Issue.objects.all()
        issues = Issue.objects.filter(
            Q(author=self.request.user) | Q(assign_to=self.request.user))

        return issues


class CommentViewset(ModelViewSet):
    """_Manage CRUD operations on Comment object

    Args:
        ModelViewSet (_type_): base viewset class to manage C.R.U.D
    """

    serializer_class = CommentSerialiser
    permission_classes = [IsAuthenticated, CommentPermission]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """Simple query_set to get all Comment if logged is author or
        if user is Issue author or if the Issue was assign to him

        Returns:
            _type_:all Comment
        """

        # comments = Comment.objects.all()
        comments = Comment.objects.filter(Q(author=self.request.user) | Q(
            issue__assign_to=self.request.user) | Q(issue__author=self.request.user))
        return comments
