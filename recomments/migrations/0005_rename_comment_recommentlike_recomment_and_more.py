# Generated by Django 5.0.3 on 2024-05-14 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recomments', '0004_recommentlike'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recommentlike',
            old_name='comment',
            new_name='recomment',
        ),
        migrations.RemoveField(
            model_name='recomment',
            name='post',
        ),
        migrations.AlterField(
            model_name='recomment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
