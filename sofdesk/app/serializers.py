from rest_framework.serializers import ModelSerializer, StringRelatedField


from app.models import Project, Contributor, Issue, Comment


class ProjectJsonSerialiser(ModelSerializer):
    author = StringRelatedField()

    class Meta:
        model = Project
        fields = "__all__"


class ProjectSerialiser(ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"


class ContributorJsonSerialiser(ModelSerializer, StringRelatedField):
    author = StringRelatedField()
    project = StringRelatedField()

    class Meta:
        model = Contributor
        fields = "__all__"


class ContributorSerialiser(ModelSerializer):

    class Meta:
        model = Contributor
        fields = "__all__"


class IssueJsonSerialiser(ModelSerializer, StringRelatedField):
    author = StringRelatedField()
    assign_to = StringRelatedField()
    project = StringRelatedField()

    class Meta:
        model = Issue
        fields = "__all__"


class IssueSerialiser(ModelSerializer):

    class Meta:
        model = Issue
        fields = "__all__"


class CommentJsonSerialiser(ModelSerializer, StringRelatedField):
    author = StringRelatedField()
    issue = StringRelatedField()

    class Meta:
        model = Comment
        fields = "__all__"


class CommentSerialiser(ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
