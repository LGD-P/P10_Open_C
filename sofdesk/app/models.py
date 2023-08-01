import uuid

from django.db import models

from authenticate.models import User


class Project(models.Model):

    TYPE_CHOICES = (
        ("back-end", "back-end"), ("front-end", "front-end"),
        ("iOS", "iOS"), ("Android", "Android")
    )
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=False, blank=True)
    description = models.TextField(max_length=2048, blank=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=15, blank=True,)
    created_time: models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contributor(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
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
        to=User, related_name='author', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=False, blank=True)
    description = models.TextField(max_length=2048, blank=True)
    assign_to = models.ForeignKey(
        User, related_name='assigned_issues', on_delete=models.CASCADE)
    priority = models.CharField(
        choices=PRIORITY_CHOICES, max_length=15, blank=True)
    tag = models.CharField(choices=TAG_CHOICES, max_length=15, blank=True)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=15, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name='issues')

    def __str__(self):
        return self.name


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    description = models.TextField(max_length=2048, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_time = models.DateTimeField(auto_now_add=True)
    issue = models.ForeignKey(
        to=Issue, on_delete=models.CASCADE, related_name='comment',)
