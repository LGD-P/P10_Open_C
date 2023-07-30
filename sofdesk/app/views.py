from rest_framework.viewsets import ModelViewSet


from authenticate.models import User
from app.models import (Project, Contributor,
                        Issue, Comment)
from app.serializers import (ProjectSerialiser, ContributorSerialiser,
                             IssueSerialiser, CommentSerialiser)


class ProjectViewset(ModelViewSet):
    """Manage CRUD operations on Project object

    Args:
        ModelViewSet (_type_): base viewset class to manage C.R.U.D
    """

    serializer_class = ProjectSerialiser

    def get_queryset(self):
        """Simple query_set to get all Project

        Returns:
            _type_:all Project
        """
        return Project.objects.all()

    def perform_create(self, serializer_class):
        """Use to creat Project and automatically
        creat Contributor linked to it.

        Args:
            serializer_class (_type_): ProjectSerializer

        """
        # Save Project instance first
        # get User et Project to creat & save a Contributor

        instance = serializer_class.save()
        author = User.objects.get(pk=instance.author_id)
        project_id = Project.objects.get(pk=instance.id)
        contributor = Contributor(author=author, project=project_id)
        contributor.save()


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
