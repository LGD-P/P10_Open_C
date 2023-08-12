from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


from django.db.models import Q
from app.models import (Project, Contributor,
                        Issue, Comment)
from app.serializers import (ProjectSerializer, ContributorSerializer,
                             IssueSerializer, CommentSerialiser)
from app.permissions import (IsContributorPermission)


class ProjectViewset(ModelViewSet):

    """Manage CRUD operations on Project object

    Args:
        ModelViewSet (_type_): base viewset class to manage C.R.U.D
    """

    serializer_class = ProjectSerializer
    permission_classes = [IsContributorPermission, IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """Filter queryset to only show contributors for the project of the logged in user"""

        projects = Project.objects.filter(
            contributor__author=self.request.user).prefetch_related('contributor_set')
        return projects


class ContributorViewset(ModelViewSet):
    """Manage CRUD operations on Contributor object

    Args:
        ModelViewSet (_type_): base viewset class to manage C.R.U.D
    """

    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """Filter queryset to only show contributors for the project of the logged in user"""

        # get the logged in user
        user = self.request.user

        # get all projects IDs for logged in user
        project_ids = Contributor.objects.filter(
            author=user).values_list('project_id', flat=True)

        # Filter the contributors to only include contributors with matching project IDs
        queryset = Contributor.objects.filter(project_id__in=project_ids).select_related(
            'author').prefetch_related('project')

        # contributors = Contributor.objects.all()
        contributors = Contributor.objects.filter(
            Q(author=self.request.user) | Q(project__author=self.request.user))

        return contributors


class IssuetViewset(ModelViewSet):
    """_Manage CRUD operations on Issue object

    Args:
        ModelViewSet (_type_): base viewset class to manage C.R.U.D
    """

    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """Simple query_set to get all Issue

        Returns:
            _type_:all Issue
        """

        return Issue.objects.filter(Q(author=self.request.user) | Q(assign_to=self.request.user))


class CommentViewset(ModelViewSet):
    """_Manage CRUD operations on Comment object

    Args:
        ModelViewSet (_type_): base viewset class to manage C.R.U.D
    """

    serializer_class = CommentSerialiser
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """Simple query_set to get all Issue

        Returns:
            _type_:all Issue
        """
        return Comment.objects.filter(
            Q(author=self.request.user) | Q(
                issue__assign_to=self.request.user) | Q(
                issue__author=self.request.user))
