# Generated by Django 4.2.3 on 2023-07-25 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_projet_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contributor',
            old_name='projet',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='projet',
            new_name='project',
        ),
    ]
