import uuid

from django.db import models

from authenticate.models import User


class Project(models.Model):

    TYPE_CHOICES = (
        ("back-end", "back-end"), ("front-end", "front-end"),
        ("iOS", "iOS"), ("Android", "Android")
    )
    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='project_author')
    name = models.CharField(max_length=128, null=False,
                            blank=True, unique=True)
    description = models.TextField(max_length=2048, blank=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=15, blank=True,)
    created_time: models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Rajouter un champ User pour attribuer un utilisateur à l'objet Contributer
class Contributor(models.Model):
    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='contributor_author')
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='contributor_user')
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name='contributor_project')
    created_time = models.DateTimeField(auto_now_add=True)


class Issue(models.Model):
    PRIORITY_CHOICES = (
        ("LOW", "LOW"), ("MEDIUM", "MEDIUM"), ("HIGH", "HIGH")
    )

    TAG_CHOICES = (
        ("BUG", "BUG"), ("FEATURE", "FEATURE"), ("TASK", "TASK")
    )

    STATUS_CHOICES = (
        ("To Do", "To Do"), ("In Progress", "In Progress"), ("Finished", "Finished")
    )

    author = models.ForeignKey(
        to=User, related_name='issue_author', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=False, blank=True)
    description = models.TextField(max_length=2048, blank=True)
    assign_to = models.ForeignKey(
        User, related_name='assigned_issue', on_delete=models.CASCADE)
    priority = models.CharField(
        choices=PRIORITY_CHOICES, max_length=15, blank=True)
    tag = models.CharField(choices=TAG_CHOICES, max_length=15, blank=True)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=15, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name='issue_project')

    def __str__(self):
        return self.name


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="comment_author")
    description = models.TextField(max_length=2048, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_time = models.DateTimeField(auto_now_add=True)
    issue = models.ForeignKey(
        to=Issue, on_delete=models.CASCADE, related_name='comment_issue',)
