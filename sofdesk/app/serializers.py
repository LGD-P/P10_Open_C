from rest_framework.serializers import (
    ModelSerializer, CurrentUserDefault)
from rest_framework.exceptions import ValidationError

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
        """
        validated_data['author'] = self.context['request'].user
        instance = super().create(validated_data)
        contributor = Contributor(
            author=instance.author, project=instance, user=instance.author)
        contributor.save()
        return instance

    def delete(self, instance):
        """Delete automaticly a Contributors
        when a project is created
        """
        contributors = Contributor.objects.filter(project=instance)
        contributors.delete()
        instance.delete()


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = "__all__"

        read_only_fields = ['author']

    def create(self, validated_data):
        author = self.context['request'].user
        user = validated_data['user']
        project = validated_data['project']

        if Contributor.objects.filter(author=author, user=user, project=project).exists():
            # Contributor already exist ==> raise error and pass
            instance = None
            message = f"Le contributeur {user.username} est déjà associé au projet."
            raise ValidationError(message)
        else:
            # New instance creation allowed
            validated_data['author'] = author
            instance = super().create(validated_data)

        return instance


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = "__all__"
        read_only_fields = ['author']

    def create(self, validated_data):

        validated_data['author'] = self.context['request'].user
        project = validated_data['project']

        instance = super().create(validated_data)

        # Check if Contributor already exist else creat it
        if Contributor.objects.filter(user=instance.assign_to, project=project).exists():
            pass
        else:
            contributor = Contributor(author=instance.author,
                                      user=instance.assign_to, project=project)
            contributor.save()

        return instance


class CommentSerialiser(ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['author']

    def create(self, validated_data):

        validated_data['author'] = self.context['request'].user
        instance = super().create(validated_data)

        return instance
