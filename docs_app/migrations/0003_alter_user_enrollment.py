# Generated by Django 4.2.6 on 2023-12-04 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs_app', '0002_alter_user_email_alter_user_phone_no_alter_user_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='enrollment',
            field=models.BigIntegerField(null=True, unique=True),
        ),
    ]
