# Generated by Django 5.0.3 on 2024-04-09 16:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment_likes', '0001_initial'),
        ('comments', '0003_alter_comment_created_at_alter_comment_updated_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment_like',
            new_name='CommentLike',
        ),
    ]