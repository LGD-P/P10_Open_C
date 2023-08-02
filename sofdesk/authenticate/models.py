from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_id = models.BigAutoField(primary_key=True)
    can_be_contacted = models.BooleanField(default=False)
    can_be_shared = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    username = models.CharField(
        max_length=50, blank=False, null=False, unique=True)

    def __str__(self) -> str:
        return self.username
