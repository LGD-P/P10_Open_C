from rest_framework.serializers import (
    ModelSerializer, CurrentUserDefault)

from django.db.models import Q

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


class ContributorSerializer(ModelSerializer):

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

        # récupérer les données du sérializer
        request = self.context.get('request')

        # Limite limite les choix de project en fonction d'author et contributor
        if request and request.user.is_authenticated:
            self.fields['project'].queryset = Project.objects.filter(
                Q(contributor__author=request.user) | Q(author=request.user))
            self.fields['author'].queryset = self.context['request'].user

    def create(self, validated_data):
        # Pas sur que ce soit utile à tester
        author = self.context['request'].user
        project = validated_data['project']

        validated_data['author'] = author

        instance = super().create(validated_data)

        # Vérifie si le contributor n'existe pas déjà auquel cas ne le crée pas
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
        read_only_fields = ['author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get('request')

        if request and request.user.is_authenticated:
            self.fields['author'].queryset = self.context['request'].user
            self.fields['issue'].queryset = Issue.objects.filter(
                assign_to=request.user)

    def create(self, validated_data):

        validated_data['author'] = self.context['request'].user
        instance = super().create(validated_data)

        return instance
