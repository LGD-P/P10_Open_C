from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "username", "can_be_contacted", "can_be_shared",
        "user_id",
    ]
    list_filter = list_display
