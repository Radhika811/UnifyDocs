# Generated by Django 4.2.6 on 2024-01-10 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docs_app', '0012_user_enabled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='editor_group',
        ),
        migrations.RemoveField(
            model_name='document',
            name='moderator_group',
        ),
        migrations.RemoveField(
            model_name='document',
            name='viewer_group',
        ),
    ]
