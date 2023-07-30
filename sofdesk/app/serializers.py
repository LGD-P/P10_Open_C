from rest_framework.serializers import ModelSerializer


from app.models import Project, Contributor, Issue, Comment


class ProjectSerialiser(ModelSerializer):
    # method creat pour le contributeur à mettre ici !!
    # depth
    class Meta:
        model = Project
        fields = "__all__"


class ContributorSerialiser(ModelSerializer):

    class Meta:
        model = Contributor
        fields = "__all__"


class IssueSerialiser(ModelSerializer):

    class Meta:
        model = Issue
        fields = "__all__"


class CommentSerialiser(ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
