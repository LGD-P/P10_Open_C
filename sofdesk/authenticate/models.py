from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_id = models.BigAutoField(primary_key=True)
    can_be_contacted = models.BooleanField(default=False)
    can_be_shared = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    age = models.PositiveBigIntegerField(blank=False, null=False, default=15)

    def __str__(self) -> str:
        return self.username
