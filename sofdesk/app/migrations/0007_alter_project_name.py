# Generated by Django 4.2.3 on 2023-08-04 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_comment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(blank=True, max_length=128, unique=True),
        ),
    ]
