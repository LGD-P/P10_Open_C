from rest_framework.serializers import ModelSerializer, StringRelatedField


from app.models import Project, Contributor, Issue, Comment


class ProjectSerialiser(ModelSerializer, StringRelatedField):
    author = StringRelatedField()

    class Meta:
        model = Project
        fields = "__all__"


class ContributorSerialiser(ModelSerializer, StringRelatedField):
    author = StringRelatedField()
    projet = StringRelatedField()

    class Meta:
        model = Contributor
        fields = "__all__"


class IssueSerialiser(ModelSerializer, StringRelatedField):
    author = StringRelatedField()
    assign_to = StringRelatedField()
    project = StringRelatedField()

    class Meta:
        model = Issue
        fields = "__all__"


class CommentSerialiser(ModelSerializer, StringRelatedField):
    author = StringRelatedField()

    class Meta:
        model = Comment
        fields = "__all__"
