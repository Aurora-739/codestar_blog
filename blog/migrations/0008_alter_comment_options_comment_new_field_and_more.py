# Generated by Django 5.2.2 on 2025-06-21 09:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_comment_challenge'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AddField(
            model_name='comment',
            name='new_field',
            field=models.SlugField(default='Default Text'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL),
        ),
    ]
