from rest_framework.viewsets import ModelViewSet


from authenticate.models import User
from app.models import (Project, Contributor,
                        Issue, Comment)
from app.serializers import (ProjectSerialiser, ProjectJsonSerialiser,
                             ContributorSerialiser, ContributorJsonSerialiser,
                             IssueSerialiser, IssueJsonSerialiser,
                             CommentSerialiser, CommentJsonSerialiser)


class ProjectViewset(ModelViewSet):

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            serializer_class = ProjectJsonSerialiser
            return serializer_class
        serializer_class = ProjectSerialiser
        return serializer_class

    def get_queryset(self):
        return Project.objects.all()

    def perform_create(self, serializer_class):
        instance = serializer_class.save()
        author = User.objects.get(pk=instance.author_id)
        project_id = Project.objects.get(pk=instance.id)
        contributor = Contributor(author=author, project=project_id)
        contributor.save()


class ContributorViewset(ModelViewSet):

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            serializer_class = ContributorJsonSerialiser
            return serializer_class
        serializer_class = ContributorSerialiser
        return serializer_class

    def get_queryset(self):
        return Contributor.objects.all()


class IssuetViewset(ModelViewSet):

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            serializer_class = IssueJsonSerialiser
            return serializer_class
        serializer_class = IssueSerialiser
        return serializer_class

    def get_queryset(self):
        return Issue.objects.all()


class CommentViewset(ModelViewSet):

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            serializer_class = CommentJsonSerialiser
            return serializer_class
        serializer_class = CommentSerialiser
        return serializer_class

    def get_queryset(self):
        return Comment.objects.all()
