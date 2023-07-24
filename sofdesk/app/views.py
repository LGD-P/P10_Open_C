from rest_framework.viewsets import ModelViewSet

from app.models import (Project, Contributor,
                        Issue, Comment)
from app.serializers import (ProjectSerialiser, ContributorSerialiser,
                             IssueSerialiser, CommentSerialiser)


class ProjectViewset(ModelViewSet):

    serializer_class = ProjectSerialiser

    def get_queryset(self):
        return Project.objects.all()


class ContributorViewset(ModelViewSet):

    serializer_class = ContributorSerialiser

    def get_queryset(self):
        return Contributor.objects.all()


class IssuetViewset(ModelViewSet):

    serializer_class = IssueSerialiser

    def get_queryset(self):
        return Issue.objects.all()


class CommentViewset(ModelViewSet):

    serializer_class = CommentSerialiser

    def get_queryset(self):
        return Comment.objects.all()
