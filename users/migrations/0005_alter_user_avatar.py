# Generated by Django 4.2.7 on 2024-01-28 13:05

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_viewhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=None, null=True, upload_to=users.models.user_avatar_path),
        ),
    ]