# Generated by Django 5.0.3 on 2024-05-14 16:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recomments', '0005_rename_comment_recommentlike_recomment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommentlike',
            name='recomment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recomment_likes', to='recomments.recomment'),
        ),
    ]
