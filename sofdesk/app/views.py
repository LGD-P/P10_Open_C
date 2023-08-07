from rest_framework.viewsets import ModelViewSet


from app.models import (Project, Contributor,
                        Issue, Comment)
from app.serializers import (ProjectSerializer, ContributorSerialiser,
                             IssueSerialiser, CommentSerialiser)
from app.permissions import (ProjectPermission)


class ProjectViewset(ModelViewSet):
    """Manage CRUD operations on Project object

    Args:
        ModelViewSet (_type_): base viewset class to manage C.R.U.D
    """

    serializer_class = ProjectSerializer
    permission_classes = [ProjectPermission]

    def get_queryset(self):
        """Simple query_set to get all Project

        Returns:
            _type_:all Project
        """
        return Project.objects.select_related('author').filter(author=self.request.user)


class ContributorViewset(ModelViewSet):
    """Manage CRUD operations on Contributor object

    Args:
        ModelViewSet (_type_): base viewset class to manage C.R.U.D
    """

    serializer_class = ContributorSerialiser

    def get_queryset(self):
        """Simple query_set to get all Contributor

        Returns:
            _type_:all Contributor
        """
        return Contributor.objects.all()


class IssuetViewset(ModelViewSet):
    """_Manage CRUD operations on Issue object

    Args:
        ModelViewSet (_type_): base viewset class to manage C.R.U.D
    """

    serializer_class = IssueSerialiser

    def get_queryset(self):
        """Simple query_set to get all Issue

        Returns:
            _type_:all Issue
        """
        return Issue.objects.all()


class CommentViewset(ModelViewSet):
    """_Manage CRUD operations on Comment object

    Args:
        ModelViewSet (_type_): base viewset class to manage C.R.U.D
    """

    serializer_class = CommentSerialiser

    def get_queryset(self):
        """Simple query_set to get all Issue

        Returns:
            _type_:all Issue
        """
        return Comment.objects.all()
