from rest_framework.serializers import ModelSerializer


from app.models import Project, Contributor, Issue, Comment


class ProjectSerialiser(ModelSerializer):
    class Meta:
        model = Project

    def create(self, validated_data):
        """Creat automaticly a Contributor
        when a new project is created

        Args:
            validated_data (_type_): Project Instance

        Returns:
            Instance: Project instance
        """
        instance = super().create(validated_data)
        contributor = Contributor(
            author=instance.author, project=instance)
        contributor.save()
        return instance


class ContributorSerialiser(ModelSerializer):

    class Meta:
        model = Contributor
        fields = "__all__"


class IssueSerialiser(ModelSerializer):

    class Meta:
        model = Issue
        fields = ['author', 'name', 'description',
                  'priority', 'tag', 'status', 'project']

    def create(self, validated_data):
        """Creat automaticly a Contributor
        when a new project is created

        Args:
            validated_data (_type_): Project Instance

        Returns:
            Instance: Project instance
        """
        instance = super().create(validated_data)
        project = validated_data.get('project')
        contributor = Contributor(
            author=instance.assign_to, project=project)
        contributor.save()
        return instance


class CommentSerialiser(ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
