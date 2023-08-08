from rest_framework.serializers import (
    ModelSerializer, CurrentUserDefault)


from app.models import Project, Contributor, Issue, Comment


class ProjectSerializer(ModelSerializer):
    author = CurrentUserDefault()

    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ["author"]

    def create(self, validated_data):
        """Creat automaticly a Contributor
        when a new project is created

        Args:
            validated_data (_type_): Project Instance

        Returns:
            Instance: Project instance
        """
        validated_data['author'] = self.context['request'].user
        instance = super().create(validated_data)
        contributor = Contributor(
            author=instance.author, project=instance)
        contributor.save()
        return instance


class ContributorSerialiser(ModelSerializer):

    class Meta:
        model = Contributor
        fields = "__all__"


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = "__all__"
        read_only_fields = ['author']

    def __init__(self, *args, **kwargs):
        """
        Override the serializer initialization to limit the available choices
        for related fields based on the logged in user.
        """
        super().__init__(*args, **kwargs)

        # Retrieve the request from the serializer context
        request = self.context.get('request')

        # Limit the available choices for the project field based on related projects
        if request and request.user.is_authenticated:
            self.fields['project'].queryset = Project.objects.filter(
                contributor__author=request.user)
            self.fields['author'].queryset = self.context['request'].user

    def create(self, validated_data):
        # Pas sur que ce soit utile à tester
        author = self.context['request'].user
        project = validated_data['project']

        validated_data['author'] = author

        instance = super().create(validated_data)

        # Check if a Contributor instance already exists for the author and project
        if Contributor.objects.filter(author=instance.assign_to, project=project).exists():
            pass
        else:
            contributor = Contributor(
                author=instance.assign_to, project=project)
            contributor.save()

        return instance


class CommentSerialiser(ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
