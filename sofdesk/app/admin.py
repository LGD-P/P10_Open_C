from django.contrib import admin

from .models import Contributor, Projet, Issue, Comment


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = ["author", "projet", "created_time"]
    list_filter = list_display


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = [
        "author", "name", "description",
        "type"]
    list_filter = list_display


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = [
        "author", "name", "description", "assign_to",
        "priority", "tag", "status", "created_time", "projet"
    ]
    list_filter = list_display


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "author", "description", "uuid",
        "created_time", "issue"]
    list_filter = list_display
